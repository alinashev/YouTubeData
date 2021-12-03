import logging
from typing import Any

from Commons.DataBase import DataBase
from Entities.Video import Video


class VideoExtractorFromDB:

    def extract(self) -> list:
        try:
            data_base: DataBase = DataBase()
            connect: Any = data_base.connect()
            cursor: Any = connect.cursor()

            query: str = """ SELECT * FROM videodata"""
            cursor.execute(query)
            rows: Any = cursor.fetchall()

            self.video_obj_list: list = [Video(rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]) for rows in rows]
            logging.info('Successfully retrieved from database')
            data_base.close()
            return self.video_obj_list
        except Exception as error:
            logging.error(error)

    def get_video_obj_list(self) -> list:
        return self.video_obj_list
