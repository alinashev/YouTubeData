from enum import Enum

from Action.Action import Action
from Analysis.Analyzer import Analyzer
from Commons.ChannelsID import ChannelsID
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoExtractorFromDB import VideoExtractorFromDB
from Load.VideoCategoryLoader import VideoCategoryLoader
from Report.Reporter import Reporter
from Transform.CategoryParser import CategoryParser


class DataReporter(Action):
    def execute(self) -> None:
        video_from_db: VideoExtractorFromDB = VideoExtractorFromDB()
        video_list_db: list = video_from_db.extract_from_bd()

        storage: StorageS3 = StorageS3()
        file_writer: FileWriter = FileWriter()
        video_category_extractor: VideoCategoryExtractor = VideoCategoryExtractor()

        file_name: str = 'videoCategory.json'

        file_writer.writing(video_category_extractor.extract(video_list_db), file_name)
        storage.load_file_to_s3(file_writer.get_path())

        reader: ReaderJSON = ReaderJSON(file_name)
        json_category: dict = reader.get_json()

        category_list: list = CategoryParser().parse_to_obj(json_category, video_list_db)

        VideoCategoryLoader().loading_to_DWH(category_list)

        channel_id: Enum = ChannelsID('channels.txt').get_channels_id()

        report_file_name = "report.json"
        analyzer: Analyzer = Analyzer()
        file_writer.writing(analyzer.get_category(channel_id, category_list), report_file_name)