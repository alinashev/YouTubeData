import unittest

from unittest.mock import patch


class TestDataBase(unittest.TestCase):

    @patch('DataPuller.DataBase.connect')
    def test_connect(self, connect) -> None:
        self.assertIsNotNone(connect)

    if __name__ == '__main__':
        unittest.main()
