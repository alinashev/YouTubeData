import json


class FileWriter:
    __path: str = None

    def writing(self, data: dict, path: str) -> None:
        self.__path = path
        with open(self.__path, 'w') as f:
            json.dump(data, f)

    def get_path(self) -> str:
        return self.__path
