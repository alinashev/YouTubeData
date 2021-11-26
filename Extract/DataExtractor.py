from abc import ABC, abstractmethod


class DataExtractor(ABC):

    @abstractmethod
    def extract(self, ChannelsID) -> dict:
        pass
