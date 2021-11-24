import requests

import settings
from ChannelsID import ChannelsID


class ChannelDataExtractor:
    __key = settings.API_key
    __part = 'statistics'
    __base_url = 'https://youtube.googleapis.com/youtube/v3/'
    __list_of_channel_id = None
    __url = None

    def __init__(self, ChannelsID):
        self.ChannelsID = ChannelsID

    @classmethod
    def channels_url_build(cls, id):
        cls.__url = cls.__base_url \
                    + 'channels?' \
                    + 'part={part}'.format(part=cls.__part) \
                    + '&key={key}'.format(key=cls.__key) \
                    + '&id={id}'.format(id=id)
        return cls.__url

    def get_channel_id_list(self):
        self.__list_of_channel_id = list(map(lambda c: c.value, self.ChannelsID))
        return self.__list_of_channel_id

    def get_url_list(self):
        return list(map(self.channels_url_build, self.get_channel_id_list()))

    def get_request_list(self):
        return list(map(requests.get, self.get_url_list()))

    def generate_json(self):
        requests_in_json_format = list(map(lambda requests_list: requests_list.json(), self.get_request_list()))
        return dict(zip(list(map(lambda c: c.name, self.ChannelsID)), requests_in_json_format))
