class Channel:
    channel_name: str
    channel_id: str
    view_count: str
    subscriber_count: str
    video_count: str

    def __init__(self, channel_name: str, channel_id: str, view_count: str, subscriber_count: str,
                 video_count: str) -> None:
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.view_count = view_count
        self.subscriber_count = subscriber_count
        self.video_count = video_count

    def __str__(self) -> str:
        return 'channel_name {channel_name}' \
               '\nchannel_id {channel_id}' \
               '\nview_count {view_count}' \
               '\nsubscriber_count {subscriber_count}' \
               '\nvideo_count {video_count}\n'.format(channel_name=self.channel_name,
                                                      channel_id=self.channel_id,
                                                      view_count=self.view_count,
                                                      subscriber_count=self.subscriber_count,
                                                      video_count=self.video_count)
