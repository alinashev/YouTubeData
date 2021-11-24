import json


class WriterToFile:
    @staticmethod
    def writing(data, file):
        with open(file, 'w') as f:
            json.dump(data, f)