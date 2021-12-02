import unittest
from typing import Any

from Commons.StorageS3 import StorageS3


class TestStorageS3(unittest.TestCase):
    directory: str = "YouTube"
    storage: Any

    def setUp(self) -> None:
        self.storage = StorageS3()
        self.storage.download_folder(self.directory)
        self.result_path_list: list = self.storage.get_path_list()

    def test_existence_dataChannels(self) -> None:
        self.assertIsNot(self.result_path_list[0].find('dataChannels'), -1)

    def test_existence_dataVideos(self) -> None:
        self.assertIsNot(self.result_path_list[1].find('dataVideos'), -1)

    def test_existence_files(self) -> None:
        self.assertIsNot(len(self.result_path_list), 0)

    def test_type_returned(self) -> None:
        self.assertEqual(type(self.result_path_list), list)

    if __name__ == '__main__':
        unittest.main()
