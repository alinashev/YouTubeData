from ChannelsID import ChannelsID
from ChannelDataExtractor import ChannelDataExtractor
from Commons.StorageS3 import StorageS3
from Commons.FileWriter import FileWriter
from VideoDataExtractor import VideoDataExtractor


def main():
    extractor_channels = ChannelDataExtractor()
    extractor_videos = VideoDataExtractor()

    file_writer = FileWriter()
    storage = StorageS3()

    file_writer.writing(extractor_channels.extract_data(ChannelsID), 'dataChannels.json')
    storage.load_file_to_s3(file_writer.get_path())

    file_writer.writing(extractor_videos.extract_data(ChannelsID), 'dataVideos.json')
    storage.load_file_to_s3(file_writer.get_path())




if __name__ == '__main__':
    main()
