from abc import ABC, abstractmethod


class Loader(ABC):
    @abstractmethod
    def loading_to_DWH(self, list_for_load: list) -> None:
        pass
