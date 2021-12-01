import json


class ReaderJSON:
    path: str
    text: dict

    def __init__(self, path: str) -> None:
        self.path = path

    def open(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = json.load(f)
        return self.text

    def get_json(self) -> dict:
        return ReaderJSON.open(self)