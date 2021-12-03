from typing import Any

from Entities.Channel import Channel
from Transform.Parser import Parser


class ChannelParser(Parser):
    def parse(self, json_string: Any, ChannelsID: dict) -> list[Channel]:
        return [Channel(channelID,
                        ChannelsID[channelID],
                        json_string[channelID]["items"][0]["statistics"]["viewCount"],
                        json_string[channelID]["items"][0]["statistics"]["subscriberCount"],
                        json_string[channelID]["items"][0]["statistics"]["videoCount"]
                        )
                for channelID in ChannelsID
                ]