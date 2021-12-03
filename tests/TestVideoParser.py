import json
import unittest

from Entities.Video import Video
from Transform.VideoParser import VideoParser


class TestVideoParser(unittest.TestCase):

    def setUp(self) -> None:
        with open('resources/dataVideos.json', 'r', encoding='utf-8') as f:
            self.json_video = json.load(f)

        self.channel_id = {line.split()[0]: line.split()[1] for line in open('resources/channels.txt')}

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