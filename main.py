from ChannelsID import ChannelsID
from ChannelDataExtractor import ChannelDataExtractor
from Commons.WriterToFile import WriterToFile
from VideoDataExtractor import VideoDataExtractor


def main():
    extractor_channels = ChannelDataExtractor(ChannelsID)
    extractor_videos = VideoDataExtractor(ChannelsID)

    WriterToFile.writing(extractor_channels.generate_json(), 'dataChannels.json')
    WriterToFile.writing(extractor_videos.generate_json(), 'dataVideos.json')


if __name__ == '__main__':
    main()
