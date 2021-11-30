import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Commons.ReaderJSON import ReaderJSON
from Entities.Channel import Channel
from Transform.ChannelParser import ChannelParser


class TestChannelParser(unittest.TestCase):
    json_channels: dict
    channel_id: Enum
    channel_parser: ChannelParser
    method_result: list
    list_of_type_result: list

    def setUp(self) -> None:
        self.json_channels = ReaderJSON('YouTube/Lake/jsonTypesFile/YouTube/dataChannels.json').get_json()
        self.channel_id = ChannelsID('channels.txt').get_channels_id()
        self.channel_parser = ChannelParser()
        self.method_result = self.channel_parser.parse(self.json_channels, self.channel_id)
        self.list_of_type_result = list(map(type, self.method_result))

    def test_non_empty_returned_result(self) -> None:
        self.assertIsNot(len(self.method_result), 0)

    def test_keys_uniqueness_check(self) -> None:
        self.assertIs(len(set(self.list_of_type_result)), 1)

    def test_check_type_object(self) -> None:
        self.assertEqual(set(self.list_of_type_result).pop(), Channel)

    if __name__ == '__main__':
        unittest.main()
