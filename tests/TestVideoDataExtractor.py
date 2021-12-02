import unittest

from Extract.VideoDataExtractor import VideoDataExtractor


class TestVideoDataExtractor(unittest.TestCase):
    channel_id: dict
    extract_data: dict

    def setUp(self) -> None:
        self.channel_id = {line.split()[0]: line.split()[1] for line in open('resources/channels.txt')}

        self.extract_data = VideoDataExtractor().extract(self.channel_id)

    def test_empty(self) -> None:
        self.assertIsNot(len(self.extract_data), 0)

    def test_return_type(self) -> None:
        self.assertEqual(type(self.extract_data), dict)

    if __name__ == '__main__':
        unittest.main()
