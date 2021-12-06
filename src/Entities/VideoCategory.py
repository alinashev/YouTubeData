class VideoCategory:

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

    def get_video_id(self) -> str:
        return self.video_id

    def get_video_category_id(self) -> str:
        return self.video_category_id

    def get_channel_name(self) -> str:
        return self.channel_name

    def get_channel_id(self) -> str:
        return self.channel_id
