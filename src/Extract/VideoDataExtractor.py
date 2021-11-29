import logging
from typing import Any

import settings
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoDataExtractor(DataExtractor):
    __youtube: Any = build('youtube', 'v3', developerKey=settings.you_tube_API_key)

    def extract(self, ChannelsID) -> dict:
        list_req: list = list()
        for channelID in ChannelsID:
            request = self.__youtube.search().list(
                part="snippet",
                channelId=channelID.value,
                maxResults="5",
                order="date"
            )
            response: Any = request.execute()
            list_req.append(response)
        logging.info("Data about video pulled")
        return dict(zip(list(map(lambda c: c.name, ChannelsID)), list_req))
