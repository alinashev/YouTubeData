from ChannelsID import ChannelsID
from ChannelDataExtractor import ChannelDataExtractor
from VideoDataExtractor import VideoDataExtractor


def main():
    extractor_channels = ChannelDataExtractor(ChannelsID)
    extractor_videos = VideoDataExtractor(ChannelsID)


if __name__ == '__main__':
    main()
