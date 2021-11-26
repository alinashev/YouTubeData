import enum
import unittest

from ChannelsID import ChannelsID


class TestChannelsID(unittest.TestCase):

    def test_get_channels_id(self) -> None:
        channel_id: enum.Enum = ChannelsID('channels.txt').get_channels_id()
        values: list = [v.value for v in channel_id]
        name: list = [n.name for n in channel_id]

        self.assertEqual(type(channel_id), enum.EnumMeta)
        self.assertIsNot(len(values), 0)
        self.assertIsNot(len(name), 0)

    if __name__ == '__main__':
        unittest.main()
