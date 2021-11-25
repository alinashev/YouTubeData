import logging

from Commons.DataBase import DataBase
from Load.Loader import Loader


class ChannelLoader(Loader):
    def loading_to_DWH(self, list_for_load):
        try:
            connect = DataBase.connect()
            cursor = connect.cursor()

            for i in list_for_load:
                obj = i
                insert_query = """INSERT INTO channel ( channel_name, channel_id, view_count, subscriber_count, video_count) VALUES (
                '{channel_name}', '{channel_id}', '{view_count}', '{subscriber_count}', '{video_count}') """.format(
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
