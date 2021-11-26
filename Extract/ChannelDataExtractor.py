import logging
import settings

from typing import Any
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class ChannelDataExtractor(DataExtractor):

    __youtube: Any = build('youtube', 'v3', developerKey=settings.you_tube_API_key)

    def extract(self, ChannelsID) -> dict:
        list_req: list = list()
        for channelID in ChannelsID:
            request: Any = self.__youtube.channels().list(
                part="statistics",
                id=channelID.value
            )
            response: Any = request.execute()
            list_req.append(response)
        logging.info("Data about channels pulled")
        return dict(zip(list(map(lambda c: c.name, ChannelsID)), list_req))

