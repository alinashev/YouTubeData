from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Parser(ABC):
    @abstractmethod
    def parse(self, json_string: Any, ChannelsID: Enum) -> list:
        pass

