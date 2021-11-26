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
        cls.path = cls.storage.get_path_list(cls.directory)

        cls.json_channels = ReaderJSON(cls.path[0]).get_json()
        cls.json_video = ReaderJSON(cls.path[1]).get_json()

    def test_open_json_file(self) -> None:
        for p in self.path:
            result: Any = ReaderJSON(p).open_json_file()
            self.assertEqual(type(result), dict)
            self.assertIsNot(len(result), 0)
            self.assertIsNot(result.keys(), 10)

    def test_get_json(self) -> None:
        self.assertEqual(type(self.json_channels), dict)
        self.assertEqual(type(self.json_video), dict)

    if __name__ == '__main__':
        unittest.main()
