import settings
from googleapiclient.discovery import build

from Extract.DataExtractor import DataExtractor


class ChannelDataExtractor(DataExtractor):

    __youtube = build('youtube', 'v3', developerKey=settings.you_tube_API_key)

    def extract_data(self, ChannelsID):
        list_req = list()
        for channelID in ChannelsID:
            request = self.__youtube.channels().list(
                part="statistics",
                id=channelID.value
            )
            response = request.execute()
            list_req.append(response)
        return dict(zip(list(map(lambda c: c.name, ChannelsID)), list_req))

