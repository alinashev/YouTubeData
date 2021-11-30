from typing import Any

from Commons.DataBase import DataBase
from Entities.Video import Video


class VideoExtractorFromDB:
    video_obj_list: list

    def extract_from_bd(self) -> Any:
        try:
            connect: Any = DataBase().connect()
            cursor: Any = connect.cursor()

            query: str = """ SELECT * FROM videodata"""
            cursor.execute(query)
            rows: Any = cursor.fetchall()

            self.video_obj_list = [Video(rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]) for rows in rows]
            return self.video_obj_list
        except Exception as error:
            print(error)

    def get_video_obj_list(self) -> list:
        return self.video_obj_list
