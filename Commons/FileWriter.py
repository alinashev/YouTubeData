import json
import os


class FileWriter:
    __path = None

    def writing(self, data, path):
        self.__path = path
        with open(self.__path, 'w') as f:
            json.dump(data, f)

    def get_path(self):
        return self.__path
