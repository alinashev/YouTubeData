import enum
import unittest

from Commons.ChannelsID import ChannelsID


class TestChannelsID(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.channel_id: enum.Enum = ChannelsID('resources/channels.txt')
        cls.channel = cls.channel_id.get_channels_id()
        cls.values: list = [v.value for v in cls.channel_id]
        cls.name: list = [n.name for n in cls.channel_id]

    def test_correct_return_value(self):
        self.assertEqual(type(self.channel), enum.EnumMeta)

    def test_non_empty_value(self):
        self.assertIsNot(len(self.values), 0)

    def test_non_empty_name(self):
        self.assertIsNot(len(self.name), 0)

    if __name__ == '__main__':
        unittest.main()
