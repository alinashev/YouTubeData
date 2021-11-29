import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Extract.VideoDataExtractor import VideoDataExtractor


class TestVideoDataExtractor(unittest.TestCase):
    channel_id: Enum
    extract_data: dict

    def setUp(self) -> None:
        self.channel_id = ChannelsID('channels.txt').get_channels_id()
        self.extract_data = VideoDataExtractor().extract(self.channel_id)

    def test_extract(self) -> None:
        self.assertIsNot(len(self.extract_data), 0)
        self.assertEqual(type(self.extract_data), dict)

    if __name__ == '__main__':
        unittest.main()