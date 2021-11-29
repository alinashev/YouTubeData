import settings

from typing import Any
from googleapiclient.discovery import build
from Action.Action import Action
from Commons.DataBase import DataBase
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Entities.Video import Video
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoExtractorFromDB import VideoExtractorFromDB
from Load.VideoCategoryLoader import VideoCategoryLoader
from Load.VideoLoader import VideoLoader
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








