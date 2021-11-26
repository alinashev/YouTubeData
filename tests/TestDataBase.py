import unittest

from Commons.DataBase import DataBase


class TestDataBase(unittest.TestCase):
    connection1: DataBase
    connection2: DataBase

    def setUp(self) -> None:
        self.connection1 = DataBase()
        self.connection2 = DataBase()

    def test_connect(self) -> None:
        self.assertIsNotNone(self.connection1.connect())
        self.assertEqual(self.connection1.connect(), self.connection2.connect())

    def tearDown(self) -> None:
        self.connection1.close()
        self.connection2.close()

    if __name__ == '__main__':
        unittest.main()
