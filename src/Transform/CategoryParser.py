from typing import Any

from Entities.VideoCategory import VideoCategory
from Transform.Parser import Parser


class CategoryParser(Parser):

    def parse(self, json_string: Any, video_obj_list: list) -> list:
        obj_list: list = list()
        for obj in video_obj_list:
            try:
                res: str = json_string[obj.get_video_id()]['items'][0]['snippet']['categoryId']
            except:
                res = str(None)
            obj_list.append(VideoCategory(obj.get_video_id(),
                                          res,
                                          obj.get_channel_name(),
                                          obj.get_channel_id()
                                          )
                            )
        return obj_list
