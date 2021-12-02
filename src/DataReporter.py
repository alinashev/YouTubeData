import logging
import settings

from datetime import datetime
from Action.Action import Action
from Analysis.Analyzer import Analyzer
from Commons.ChannelsID import ChannelsID
from Commons.DataBase import DataBase
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoExtractorFromDB import VideoExtractorFromDB
from Load.VideoCategoryLoader import VideoCategoryLoader
from Report.Repeater import Repeater
from Report.Reporter import Reporter
from Transform.CategoryParser import CategoryParser


class DataReporter(Action):
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

        video_from_db: VideoExtractorFromDB = VideoExtractorFromDB()
        video_list_db: list = video_from_db.extract_from_bd()

        storage: StorageS3 = StorageS3()
        file_writer: FileWriter = FileWriter()
        video_category_extractor: VideoCategoryExtractor = VideoCategoryExtractor()

        file_name: str = 'videoCategory.json'
        file_writer.writing(video_category_extractor.extract(video_list_db), file_name)
        storage.upload(file_writer.get_path())

        reader: ReaderJSON = ReaderJSON(file_name)
        json_category: dict = reader.get_json()

        category_list: list = CategoryParser().parse(json_category, video_list_db)

        VideoCategoryLoader().load(category_list)
        DataBase.close()

        channel_id: dict = ChannelsID('channels.txt').get_channels_id()

        report_file_name: str = "report.json"
        analyzer: Analyzer = Analyzer()
        file_writer.writing(analyzer.get_category(channel_id, category_list), report_file_name)

        repeater = Repeater()
        report = Reporter(report_file_name, settings.email_recipient)
        repeater.repeat(3600, lambda *args, **kwargs: report.send())
