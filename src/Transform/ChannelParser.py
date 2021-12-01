from typing import Any

from Entities.Channel import Channel
from Transform.Parser import Parser


class ChannelParser(Parser):
    def parse(self, json_string: Any, ChannelsID: Any) -> list[Channel]:
        return [Channel(channelID.name,
                        channelID.value,
                        json_string[channelID.name]["items"][0]["statistics"]["viewCount"],
                        json_string[channelID.name]["items"][0]["statistics"]["subscriberCount"],
                        json_string[channelID.name]["items"][0]["statistics"]["videoCount"]
                        )
                for channelID in ChannelsID
                ]
