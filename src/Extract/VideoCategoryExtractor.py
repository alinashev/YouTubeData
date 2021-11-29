from typing import Any

import settings
from Extract.DataExtractor import DataExtractor
from Extract.VideoExtractorFromDB import VideoExtractorFromDB
from typing import Any
from googleapiclient.discovery import build


class VideoCategoryExtractor(DataExtractor):
    __youtube: Any = build('youtube', 'v3', developerKey=settings.you_tube_API_key)


    def extract(self, video_id_list) -> dict:
        list_req: list = list()
        list_video_id = list()

        for video_id in video_id_list:
            request = self.__youtube.videos().list(
                part="id,snippet",
                id=video_id.get_video_id(),
            )
            response: Any = request.execute()

            list_req.append(response)
            list_video_id.append(video_id.get_video_id())

        return dict(zip(list_video_id, list_req))
