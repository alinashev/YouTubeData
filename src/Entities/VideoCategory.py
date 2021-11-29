class VideoCategory:
    video_id: str
    video_category_id: str
    channel_name: str
    channel_id: str

    def __init__(self, video_id, video_category_id, channel_name, channel_id) -> None:
        self.video_id = video_id
        self.video_category_id = video_category_id
        self.channel_name = channel_name
        self.channel_id = channel_id

    def __str__(self) -> str:
        return 'video_id {video_id}' \
               '\nvideo_category_id {video_category_id}' \
               '\nchannel_name {channel_name}' \
               '\nchannel_id {channel_id}\n'.format(video_id=self.video_id,
                                                    video_category_id=self.video_category_id,
                                                    channel_name=self.channel_name,
                                                    channel_id=self.channel_id)
