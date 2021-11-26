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

    def setup(self):
        self.storage = StorageS3()
        self.storage.download_folder(self.directory)
        self.path = self.storage.get_path_list(self.directory)

        self.json_channels = ReaderJSON(self.path[0]).get_json()
        self.json_video = ReaderJSON(self.path[1]).get_json()

    def test_open_json_file(self):
        self.setup()

        for p in self.path:
            result: Any = ReaderJSON(p).open_json_file()
            self.assertEqual(type(result), dict)
            self.assertIsNot(len(result), 0)
            self.assertIsNot(result.keys(), 10)

    def test_get_json(self):
        self.assertEqual(type(self.json_channels), dict)
        self.assertEqual(type(self.json_video), dict)

    if __name__ == '__main__':
        unittest.main()
