import logging
from typing import Any

from Commons.DataBase import DataBase
from Load.Loader import Loader


class ChannelLoader(Loader):
    def load(self, list_for_load: list) -> None:
        try:
            connect: Any = DataBase.connect()
            cursor: Any = connect.cursor()

            for obj in list_for_load:
                insert_query = """INSERT INTO channel ( channel_name, channel_id, view_count, subscriber_count, 
                video_count) VALUES ( '{channel_name}', '{channel_id}', '{view_count}', '{subscriber_count}', 
                '{video_count}') """.format(
                    channel_name=obj.channel_name,
                    channel_id=obj.channel_id,
                    view_count=obj.view_count,
                    subscriber_count=obj.subscriber_count,
                    video_count=obj.video_count
                )

                cursor.execute(insert_query)
                connect.commit()
            logging.info('Successfully inserted')
        except Exception as error:
            logging.error(error)
