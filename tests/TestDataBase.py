import unittest

from unittest.mock import patch
from Commons.DataBase import DataBase


class TestDataBase(unittest.TestCase):

    @patch('Commons.DataBase')
    def test_connect(self, MockDataBase) -> None:
        database = MockDataBase()
        self.assertIsNotNone(database.connect)

    if __name__ == '__main__':
        unittest.main()
