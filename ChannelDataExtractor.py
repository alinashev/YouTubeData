import settings
from DataExtractor import DataExtractor


class ChannelDataExtractor(DataExtractor):
    __key = settings.API_key
    __part = 'statistics'
    __base_url = 'https://youtube.googleapis.com/youtube/v3/'
    __list_of_channel_id = None
    __url = None

    def __init__(self, ChannelsID):
        super().__init__(ChannelsID)

    def url_build(self, channelID):
        self.__url = self.__base_url \
                     + 'channels?' \
                     + 'part={part}'.format(part=self.__part) \
                     + '&key={key}'.format(key=self.__key) \
                     + '&id={id}'.format(id=channelID)
        return self.__url

    def get_channel_id_list(self):
        return super(ChannelDataExtractor, self).get_channel_id_list()

    def get_url_list(self):
        return super(ChannelDataExtractor, self).get_url_list()

    def get_request_list(self):
        return super(ChannelDataExtractor, self).get_request_list()

    def generate_json(self):
        return super(ChannelDataExtractor, self).generate_json()
