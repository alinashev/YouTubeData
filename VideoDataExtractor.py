import requests

import settings


class VideoDataExtractor:
    __key = settings.API_key
    __part = 'snippet'
    __maxResults = 5
    __list_of_channel_id = None

    __base_url = 'https://youtube.googleapis.com/youtube/v3/'
    __url = None

    def __init__(self, ChannelsID):
        self.ChannelsID = ChannelsID


    def videos_url_build(cls, channelId):
        cls.__url = cls.__base_url \
                + 'search?' \
                + 'part={part}'.format(part=cls.__part) \
                + '&key={key}'.format(key=cls.__key)\
                + '&channelId={channelId}'.format(channelId=channelId) \
                + '&maxResults={maxResults}'.format(maxResults=cls.__maxResults)\
                + '&order=date'
        return cls.__url

    def get_channel_id_list(self):
        self.__list_of_channel_id = list(map(lambda c: c.value, self.ChannelsID))
        return self.__list_of_channel_id

    def get_url_list(self):
        return list(map(self.videos_url_build, self.get_channel_id_list()))

    def get_request_list(self):
        return list(map(requests.get, self.get_url_list()))

    def generate_json(self):
        requests_in_json_format = list(map(lambda requests_list: requests_list.json(), self.get_request_list()))
        return dict(zip(list(map(lambda c: c.name, self.ChannelsID)), requests_in_json_format))


