import logging

from Commons.DataBase import DataBase
from Load.Loader import Loader


class VideoLoader(Loader):
    def loading_to_DWH(self, list_for_load):
        try:
            connect = DataBase.connect()
            cursor = connect.cursor()

            for i in list_for_load:
                obj = i
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
        except Exception as error:
            logging.error(error)
