import logging
from datetime import datetime
from enum import Enum

import settings
from Action.Action import Action
from Commons.ChannelsID import ChannelsID
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


class DataPuller(Action):
    def execute(self) -> None:
        time: datetime = datetime.utcnow()
        log_file_name: str = settings.log_file_name.format(year=time.year,
                                                           month=time.month,
                                                           day=time.day,
                                                           hour=time.hour,
                                                           minute=time.minute,
                                                           second=time.second)

        logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        channel_id: Enum = ChannelsID('channels.txt').get_channels_id()

        extractor_channels: ChannelDataExtractor = ChannelDataExtractor()
        extractor_videos: VideoDataExtractor = VideoDataExtractor()

        file_writer: FileWriter = FileWriter()
        storage: StorageS3 = StorageS3()

        file_writer.writing(extractor_channels.extract(channel_id), 'dataChannels.json')
        storage.upload(file_writer.get_path())

        file_writer.writing(extractor_videos.extract(channel_id), 'dataVideos.json')
        storage.upload(file_writer.get_path())

        storage.download_folder("YouTube")

        path: list[str] = storage.get_path_list()

        reader_channel: ReaderJSON = ReaderJSON(path[0])
        reader_video: ReaderJSON = ReaderJSON(path[1])

        json_channels: dict = reader_channel.get_json()
        json_video: dict = reader_video.get_json()

        ChannelLoader().load(ChannelParser().parse(json_channels, channel_id))
        VideoLoader().load(VideoParser().parse(json_video, channel_id))

        DataBase.close()
