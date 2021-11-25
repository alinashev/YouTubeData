from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse_to_obj(self, json_string):
        pass

