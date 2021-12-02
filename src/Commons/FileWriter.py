import json


class FileWriter:
    __path: str

    def __init__(self, path: str) -> None:
        self.__path = path

    def writing(self, data: dict) -> None:
        with open(self.__path, 'w') as f:
            json.dump(data, f)

    def get_path(self) -> str:
        return self.__path
