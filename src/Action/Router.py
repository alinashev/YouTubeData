from Action.DataReporter import DataReporter
from Action.DataPuller import DataPuller


class Router:
    def __init__(self, version: int) -> None:
        self.version = version

    def generate_menu(self) -> None:
        self.menu = {1: DataPuller(),
                     2: DataReporter()}

    def selection_version(self) -> None:
        self.menu[self.version].execute()
