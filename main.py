import logging
from datetime import datetime

from ChannelsID import ChannelsID
from Commons.DataBase import DataBase
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.ChannelDataExtractor import ChannelDataExtractor
from Extract.VideoDataExtractor import VideoDataExtractor
from Load.ChannelLoader import ChannelLoader
from Load.VideoLoader import VideoLoader
from Transform.ChannelParser import ChannelParser
from Transform.VideoParser import VideoParser


def main():
    time = datetime.utcnow()
    log_file_name = '{year}-{month}-{day}UTC{hour}-{minute}-{second}.log'.format(year=time.year,
                                                                                 month=time.month,
                                                                                 day=time.day,
                                                                                 hour=time.hour,
                                                                                 minute=time.minute,
                                                                                 second=time.second)

    logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    channel_id = ChannelsID("channels.txt").get_channels_id()

    extractor_channels = ChannelDataExtractor()
    extractor_videos = VideoDataExtractor()

    file_writer = FileWriter()
    storage = StorageS3()

    file_writer.writing(extractor_channels.extract_data(channel_id), 'dataChannels.json')
    storage.load_file_to_s3(file_writer.get_path())

    file_writer.writing(extractor_videos.extract_data(channel_id), 'dataVideos.json')
    storage.load_file_to_s3(file_writer.get_path())

    storage = StorageS3()

    directory = "YouTube"
    storage.download_folder(directory)
    path = storage.get_path_list(directory)

    reader_channel = ReaderJSON(path[0])
    reader_video = ReaderJSON(path[1])

    json_channels = reader_channel.get_json()
    json_video = reader_video.get_json()
    ChannelLoader().loading_to_DWH(ChannelParser().parse_to_obj(json_channels, channel_id))
    VideoLoader().loading_to_DWH(VideoParser().parse_to_obj(json_video, channel_id))
    DataBase.close()


if __name__ == '__main__':
    main()
