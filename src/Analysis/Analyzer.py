from enum import Enum


class Analyzer:
    def get_category(self, ChannelsID: Enum, category_list: list) -> dict:
        category_for_channel = list()
        total_category = list()

        for ch in ChannelsID:
            for category in category_list:
                if ch.name != category.get_channel_name():
                    continue
                category_for_channel.append(category.get_video_category_id())
            category_for_channel = list(filter(lambda a: a != 'None', category_for_channel))
            total_category.append(max(category_for_channel, key=category_for_channel.count))
            category_for_channel.clear()
        return dict(zip(list(map(lambda c: c.name, ChannelsID)), total_category))

