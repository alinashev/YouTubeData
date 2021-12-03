class Video:

    def __init__(self, channel_name: str, channel_id: str, video_id: str, published_at: str, title: str,
                 description: str) -> None:
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.video_id = video_id
        self.published_at = published_at
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return 'channel_name {channel_name}' \
               '\nchannel_id {channel_id}' \
               '\nvideo_id {video_id}' \
               '\npublished_at {published_at}' \
               '\ntitle {title}\n' \
               '\ndescription {description}\n'.format(channel_name=self.channel_name,
                                                      channel_id=self.channel_id,
                                                      video_id=self.video_id,
                                                      published_at=self.published_at,
                                                      title=self.title,
                                                      description=self.description)
