import logging

from datetime import datetime
from Action.Action import Action
from Analysis.Analyzer import Analyzer
from Commons.ChannelsID import ChannelsID
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoExtractorFromDB import VideoExtractorFromDB
from Load.VideoCategoryLoader import VideoCategoryLoader
from Report.Repeater import Repeater
from Report.Reporter import Reporter
from Settings import settings, report_settings
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
        video_list_db: list = video_from_db.extract()

        storage: StorageS3 = StorageS3()
        file_writer: FileWriter = FileWriter('videoCategory.json')
        video_category_extractor: VideoCategoryExtractor = VideoCategoryExtractor()

        file_writer.writing(video_category_extractor.extract(video_list_db))
        storage.upload(file_writer.get_path())

        reader: ReaderJSON = ReaderJSON(file_writer.get_path())
        json_category: dict = reader.get_json()

        category_list: list = CategoryParser().parse(json_category, video_list_db)
        VideoCategoryLoader().load(category_list)

        channel_id: dict = ChannelsID('channels.txt').get_channels_id()

        report_file_writer = FileWriter('report.json')
        analyzer: Analyzer = Analyzer()
        report_file_writer.writing(analyzer.get_category(channel_id, category_list))

        report = Reporter(report_file_writer.get_path(), report_settings.email_recipient)

        repeater = Repeater(3600, lambda *args, **kwargs: report.send())
        repeater.repeat()
