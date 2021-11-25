import logging

import settings
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoDataExtractor(DataExtractor):
    __youtube = build('youtube', 'v3', developerKey=settings.you_tube_API_key)

    def extract_data(self, ChannelsID):
        list_req = list()
        for channelID in ChannelsID:
            request = self.__youtube.search().list(
                part="snippet",
                channelId=channelID.value,
                maxResults="5",
                order="date"
            )
            response = request.execute()
            list_req.append(response)
        logging.info("Data about video pulled")
        return dict(zip(list(map(lambda c: c.name, ChannelsID)), list_req))
