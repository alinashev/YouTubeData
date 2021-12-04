import unittest

from Commons.ReaderJSON import ReaderJSON


class TestReaderJSON(unittest.TestCase):

    def setUp(self) -> None:
        self.reader_channels = ReaderJSON('resources/dataVideos.json')
        self.reader_video = ReaderJSON('resources/dataVideos.json')

        self.open_channels = self.reader_channels.open()
        self.open_video = self.reader_video.open()

        self.json_channels = self.reader_channels.get_json()
        self.json_video = self.reader_video.get_json()

    def test_exception_missing_file(self) -> None:
        self.assertRaises(FileNotFoundError, lambda: ReaderJSON('missing.json'))

    def test_exception_invalid_json(self) -> None:
        self.assertRaises(ValueError, lambda: ReaderJSON('resources/invalid.json').open())

    def test_return_type_open_dataChannels(self) -> None:
        self.assertEqual(type(self.open_channels), dict)

    def test_return_type_open_dataVideos(self) -> None:
        self.assertEqual(type(self.open_video), dict)

    def test_empty_result_dataChannels(self) -> None:
        self.assertIsNot(len(self.open_channels), 0)

    def test_empty_result_dataVideos(self) -> None:
        self.assertIsNot(len(self.open_video), 0)

    def test_keys_amount_json_channels_file(self) -> None:
        self.assertIs(len(self.json_channels.keys()), 10)

    def test_keys_amount_json_video_file(self) -> None:
        self.assertIs(len(self.json_video.keys()), 10)

    def test_type_returned_json_channels_file(self) -> None:
        self.assertEqual(type(self.json_channels), dict)

    def test_type_returned_json_video_file(self) -> None:
        self.assertEqual(type(self.json_video), dict)

    if __name__ == '__main__':
        unittest.main()
