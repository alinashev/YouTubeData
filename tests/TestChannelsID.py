import unittest

from Commons.ChannelsID import ChannelsID


class TestChannelsID(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.channel_id: ChannelsID = ChannelsID('resources/channels.txt')
        cls.channel: dict = cls.channel_id.get_channels_id()
        cls.values: list = [cls.channel[v] for v in cls.channel]
        cls.name: list = [n for n in cls.channel]

    def test_correct_return_value(self):
        self.assertEqual(type(self.channel), dict)

    def test_non_empty_value(self):
        self.assertIsNot(len(self.values), 0)

    def test_non_empty_name(self):
        self.assertIsNot(len(self.name), 0)

    if __name__ == '__main__':
        unittest.main()