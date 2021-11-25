from ChannelsID import ChannelsID
from Entities.Channel import Channel
from Transform.Parser import Parser


class ChannelParser(Parser):
    def parse_to_obj(self, json_string):
        return [Channel(channelID.name,
                        channelID.value,
                        json_string[channelID.name]["items"][0]["statistics"]["viewCount"],
                        json_string[channelID.name]["items"][0]["statistics"]["subscriberCount"],
                        json_string[channelID.name]["items"][0]["statistics"]["videoCount"]
                        )
                for channelID in ChannelsID
                ]
