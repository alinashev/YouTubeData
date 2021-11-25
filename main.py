import logging
from datetime import datetime

from ChannelsID import ChannelsID
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.ChannelDataExtractor import ChannelDataExtractor
from Extract.VideoDataExtractor import VideoDataExtractor


def main():
    time = datetime.utcnow()
    log_file_name = 'YouTubeData-{year}-{month}-{day}UTC{hour}-{minute}-{second}.log'.format(year=time.year,
                                                                                 month=time.month,
                                                                                 day=time.day,
                                                                                 hour=time.hour,
                                                                                 minute=time.minute,
                                                                                 second=time.second)

    logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    extractor_channels = ChannelDataExtractor()
    extractor_videos = VideoDataExtractor()

    file_writer = FileWriter()
    storage = StorageS3()

    file_writer.writing(extractor_channels.extract_data(ChannelsID), 'dataChannels.json')
    storage.load_file_to_s3(file_writer.get_path())

    file_writer.writing(extractor_videos.extract_data(ChannelsID), 'dataVideos.json')
    storage.load_file_to_s3(file_writer.get_path())

    directory = "YouTube"
    storage.download_folder(directory)
    path = storage.get_path_list(directory)

    reader_channel = ReaderJSON(path[0])
    reader_video = ReaderJSON(path[1])

    json_channels = reader_channel.get_json()
    json_video = reader_video.get_json()


if __name__ == '__main__':
    main()
