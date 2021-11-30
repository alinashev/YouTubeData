from abc import ABC, abstractmethod


class Loader(ABC):
    @abstractmethod
    def load(self, list_for_load: list) -> None:
        pass
