import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Commons.ReaderJSON import ReaderJSON
from Entities.Channel import Channel
from Transform.ChannelParser import ChannelParser


class TestChannelParser(unittest.TestCase):
    json_channels: dict
    channel_id: Enum
    method_result: list
    channel_parser: ChannelParser

    def setUp(self) -> None:
        self.json_channels = ReaderJSON('YouTube/Lake/jsonTypesFile/YouTube/dataChannels.json').get_json()
        self.channel_id = ChannelsID('channels.txt').get_channels_id()
        self.channel_parser = ChannelParser()

    def test_parse_to_obj(self) -> None:
        self.method_result = self.channel_parser.parse(self.json_channels, self.channel_id)
        list_of_type_result = list(map(type, self.method_result))

        self.assertIsNot(len(self.method_result), 0)
        self.assertIs(len(set(list_of_type_result)), 1)
        self.assertEqual(set(list_of_type_result).pop(), Channel)

    if __name__ == '__main__':
        unittest.main()
