import requests
import settings

from abc import ABC, abstractmethod


class DataExtractor(ABC):
    __list_of_channel_id = None

    def __init__(self, ChannelsID):
        self.ChannelsID = ChannelsID

    @abstractmethod
    def url_build(self, ChannelsID):
        pass

    def get_channel_id_list(self):
        self.__list_of_channel_id = list(map(lambda c: c.value, self.ChannelsID))
        return self.__list_of_channel_id

    def get_url_list(self):
        return list(map(self.url_build, self.get_channel_id_list()))

    def get_request_list(self):
        return list(map(requests.get, self.get_url_list()))

    def generate_json(self):
        requests_in_json_format = list(map(lambda requests_list: requests_list.json(), self.get_request_list()))
        return dict(zip(list(map(lambda c: c.name, self.ChannelsID)), requests_in_json_format))
