from typing import Any

from Entities.Video import Video
from Transform.Parser import Parser


class VideoParser(Parser):
    def parse_to_obj(self, json_string: Any, ChannelsID: Any) -> list[Video]:
        return [Video(channelID.name,
                      channelID.value,
                      str(None),
                      json_string[channelID.name]['items'][i]['snippet']['publishedAt'],
                      json_string[channelID.name]['items'][i]['snippet']['title'],
                      str(None)
                      )
                for channelID in ChannelsID
                for i in range(0, 5)]
