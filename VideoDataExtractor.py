import settings
from DataExtractor import DataExtractor


class VideoDataExtractor(DataExtractor):
    __key = settings.API_key
    __part = 'snippet'
    __maxResults = 5
    __list_of_channel_id = None

    __base_url = 'https://youtube.googleapis.com/youtube/v3/'
    __url = None

    def __init__(self, ChannelsID):
        super().__init__(ChannelsID)

    def url_build(self, channelID):
        self.__url = self.__base_url \
                     + 'search?' \
                     + 'part={part}'.format(part=self.__part) \
                     + '&key={key}'.format(key=self.__key) \
                     + '&channelId={channelId}'.format(channelId=channelID) \
                     + '&maxResults={maxResults}'.format(maxResults=self.__maxResults) \
                     + '&order=date'
        return self.__url
        pass

    def get_channel_id_list(self):
        return super(VideoDataExtractor, self).get_channel_id_list()

    def get_url_list(self):
        return super(VideoDataExtractor, self).get_url_list()

    def get_request_list(self):
        return super(VideoDataExtractor, self).get_request_list()

    def generate_json(self):
        return super(VideoDataExtractor, self).generate_json()