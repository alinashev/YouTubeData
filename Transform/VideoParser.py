from ChannelsID import ChannelsID
from Entities.Video import Video
from Transform.Parser import Parser


class VideoParser(Parser):
    def parse_to_obj(self, json_string):
        return [Video(channelID.name,
                      channelID.value,
                      None,
                      json_string[channelID.name]['items'][i]['snippet']['publishedAt'],
                      json_string[channelID.name]['items'][i]['snippet']['title'],
                      json_string[channelID.name]['items'][i]['snippet']['description']
                      )
                for channelID in ChannelsID
                for i in range(0, 5)]
