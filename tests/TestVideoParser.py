import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Commons.ReaderJSON import ReaderJSON
from Entities.Video import Video
from Transform.VideoParser import VideoParser


class TestVideoParser(unittest.TestCase):
    json_video: dict
    channel_id: Enum
    video_parser: VideoParser
    method_result: list
    list_of_type_result: list

    def setUp(self) -> None:
        self.json_video = ReaderJSON('YouTube/Lake/jsonTypesFile/YouTube/dataVideos.json').get_json()
        self.channel_id = ChannelsID('channels.txt').get_channels_id()
        self.video_parser = VideoParser()
        self.method_result = VideoParser().parse(self.json_video, self.channel_id)
        self.list_of_type_result = list(map(type, self.method_result))

    def test_non_empty_returned_result(self) -> None:
        self.assertIsNot(len(self.method_result), 0)

    def test_keys_uniqueness_check(self) -> None:
        self.assertIs(len(set(self.list_of_type_result)), 1)

    def test_check_type_object(self) -> None:
        self.assertEqual(set(self.list_of_type_result).pop(), Video)

    if __name__ == '__main__':
        unittest.main()
