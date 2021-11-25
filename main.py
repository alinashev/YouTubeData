from ChannelsID import ChannelsID
from ChannelDataExtractor import ChannelDataExtractor
from Commons.StorageS3 import StorageS3
from Commons.WriterToFile import WriterToFile
from VideoDataExtractor import VideoDataExtractor


def main():
    extractor_channels = ChannelDataExtractor()
    extractor_videos = VideoDataExtractor()

    writer_to_file = WriterToFile()

    writer_to_file.writing(extractor_channels.extract_data(ChannelsID), 'dataChannels.json')
    writer_to_file.writing(extractor_videos.extract_data(ChannelsID), 'dataVideos.json')


if __name__ == '__main__':
    main()
