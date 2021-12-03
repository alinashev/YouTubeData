import logging
from typing import Any

from Commons.DataBase import DataBase
from Load.Loader import Loader


class VideoLoader(Loader):
    def load(self, list_for_load: list) -> None:
        try:
            data_base: DataBase = DataBase()
            connect: Any = data_base.connect()
            cursor: Any = connect.cursor()

            for obj in list_for_load:
                insert_query = """INSERT INTO videodata (channel_name, channel_id, video_id, published_at, title, 
                description) VALUES ('{channel_name}', '{channel_id}', '{video_id}', '{published_at}', '{title}', 
                '{description}') """.format(
                    channel_name=obj.channel_name,
                    channel_id=obj.channel_id,
                    video_id=obj.video_id,
                    published_at=str(obj.published_at),
                    title=str(obj.title),
                    description=str(obj.description)
                )

                cursor.execute(insert_query)
                connect.commit()
            logging.info('Successfully inserted')
            data_base.close()
        except Exception as error:
            logging.error(error)
