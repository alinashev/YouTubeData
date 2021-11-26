import json


class ReaderJSON:
    path: str
    text: str

    def __init__(self, path: str) -> None:
        self.path = path

    def open_json_file(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = json.load(f)
        return self.text

    def get_json(self) -> str:
        return ReaderJSON.open_json_file(self)
