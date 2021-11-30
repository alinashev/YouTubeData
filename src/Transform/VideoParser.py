from typing import Any

from Entities.Video import Video
from Transform.Parser import Parser


class VideoParser(Parser):
    def parse(self, json_string: Any, ChannelsID: Any) -> list[Video]:
        obj_list = list()
        for channelID in ChannelsID:
            for i in range(0, 5):
                try:
                    res: str = (json_string[channelID.name]['items'][i]['id']['videoId'])
                except:
                    res = str(None)

                obj_list.append(Video(channelID.name,
                                      channelID.value,
                                      res,
                                      json_string[channelID.name]['items'][i]['snippet']['publishedAt'],
                                      json_string[channelID.name]['items'][i]['snippet']['title'],
                                      str(None)
                                      )
                                )
        return obj_list
