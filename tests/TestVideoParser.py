import unittest
from enum import Enum

from Commons.ChannelsID import ChannelsID
from Commons.ReaderJSON import ReaderJSON
from Entities.Video import Video
from Transform.VideoParser import VideoParser


class TestVideoParser(unittest.TestCase):
    json_video: dict
    channel_id: Enum
    method_result: list
    video_parser: VideoParser

    def setUp(self) -> None:
        self.json_video = ReaderJSON('YouTube/Lake/jsonTypesFile/YouTube/dataVideos.json').get_json()
        self.channel_id = ChannelsID('channels.txt').get_channels_id()
        self.video_parser = VideoParser()

    def test_parse_to_obj(self) -> None:
        self.method_result = VideoParser().parse(self.json_video, self.channel_id)
        list_of_type_result = list(map(type, self.method_result))

        self.assertIsNot(len(self.method_result), 0)
        self.assertIs(len(set(list_of_type_result)), 1)
        self.assertEqual(set(list_of_type_result).pop(), Video)

    if __name__ == '__main__':
        unittest.main()