import unittest

from Commons.StorageS3 import StorageS3


class TestStorageS3(unittest.TestCase):
    directory: str = "YouTube"
    storage: StorageS3

    def setup(self) -> None:
        self.storage = StorageS3()
        self.storage.download_folder(self.directory)

    def test_get_path_list(self):
        self.setup()
        result_path_list: list = self.storage.get_path_list(self.directory)

        self.assertIsNot(result_path_list[0].find('dataChannels'), -1)
        self.assertIsNot(result_path_list[1].find('dataVideos'), -1)
        self.assertIsNot(len(result_path_list), 0)
        self.assertEqual(type(result_path_list), list)

    if __name__ == '__main__':
        unittest.main()
