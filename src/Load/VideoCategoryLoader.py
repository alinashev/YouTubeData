import logging

from typing import Any
from Commons.DataBase import DataBase
from Load.Loader import Loader


class VideoCategoryLoader(Loader):
    def load(self, list_for_load: list) -> None:
        try:
            connect: Any = DataBase.connect()
            cursor: Any = connect.cursor()

            for obj in list_for_load:
                insert_query = """INSERT INTO videocategory (video_id, video_category_id, channel_name, channel_id)
                 VALUES ('{video_id}', '{video_category_id}', '{channel_name}', '{channel_id}') """.format(
                    video_id=str(obj.video_id),
                    video_category_id=str(obj.video_category_id),
                    channel_name=str(obj.channel_name),
                    channel_id=str(obj.channel_id)
                )
                cursor.execute(insert_query)
                connect.commit()
            logging.info('Successfully inserted')
        except Exception as error:
            logging.error(error)
