class Analyzer:
    def get_category(self, channel_id: dict, category_id: dict, category_list: list) -> dict:
        channel_list: list = list(map(lambda c: c, channel_id))
        channel_category_dict: dict[str, list] = {j: list() for j in channel_list}
        for i in category_list:
            name = i.get_channel_name()
            if name in channel_category_dict:
                channel_category_dict[name].append(i.get_video_category_id())

        for i in channel_category_dict:
            channel_category_dict[i] = list(filter(lambda a: a != 'None', channel_category_dict[i]))
            total = max(channel_category_dict[i], key=channel_category_dict[i].count)
            channel_category_dict[i].clear()
            channel_category_dict[i].append(total)

            id = channel_category_dict[i][0]
            if id in category_id:
                channel_category_dict[i].append(category_id[id])

        return channel_category_dict
