import unittest

from Commons.DataBase import DataBase


class TestDataBase(unittest.TestCase):
    connection1: DataBase
    connection2: DataBase

    def setup(self):
        self.connection1 = DataBase()
        self.connection2 = DataBase()

    def test_connect(self):
        self.setup()

        self.assertIsNotNone(self.connection1.connect())
        self.assertEqual(self.connection1.connect(), self.connection2.connect())

    if __name__ == '__main__':
        unittest.main()
