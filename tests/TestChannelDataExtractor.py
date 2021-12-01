import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Extract.ChannelDataExtractor import ChannelDataExtractor


class TestChannelDataExtractor(unittest.TestCase):
    channel_id: Enum
    extract_data: dict

    def setUp(self) -> None:
        self.channel_id = Enum('ChannelsID',
                               {line.split()[0]: line.split()[1] for line in open('resources/channels.txt')})

        self.extract_data = ChannelDataExtractor().extract(self.channel_id)

    def test_empty(self) -> None:
        self.assertIsNot(len(self.extract_data), 0)

    def test_return_type(self) -> None:
        self.assertEqual(type(self.extract_data), dict)

    if __name__ == '__main__':
        unittest.main()
