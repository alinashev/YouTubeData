import unittest
from typing import Any

from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3


class TestReaderJSON(unittest.TestCase):
    directory: str = "YouTube"
    storage: StorageS3
    path: list
    json: dict
    json_channels: dict
    json_video: dict

    @classmethod
    def setUpClass(cls) -> None:
        cls.storage = StorageS3()
        cls.storage.download_folder(cls.directory)
        cls.path = cls.storage.get_path_list()

        cls.json_channels = ReaderJSON(cls.path[0]).get_json()
        cls.json_video = ReaderJSON(cls.path[1]).get_json()

        cls.result_channels: Any = ReaderJSON(cls.path[0]).open_json_file()
        cls.result_video: Any = ReaderJSON(cls.path[1]).open_json_file()

    def test_return_type_open_dataChannels(self) -> None:
        self.assertEqual(type(self.result_channels), dict)

    def test_return_type_open_dataVideos(self) -> None:
        self.assertEqual(type(self.result_video), dict)

    def test_empty_result_dataChannels(self) -> None:
        self.assertIsNot(len(self.result_channels), 0)

    def test_empty_result_dataVideos(self) -> None:
        self.assertIsNot(len(self.result_video), 0)

    def test_keys_amount_dataChannels(self) -> None:
        self.assertIs(len(self.result_channels.keys()), 10)

    def test_keys_amount_dataVideos(self) -> None:
        self.assertIs(len(self.result_video.keys()), 10)

    def test_type_returned_json_channels_file(self) -> None:
        self.assertEqual(type(self.json_channels), dict)

    def test_type_returned_json_video_file(self) -> None:
        self.assertEqual(type(self.json_video), dict)

    if __name__ == '__main__':
        unittest.main()
