import json
from typing import Any


class ReaderJSON:
    path: str
    text: str

    def __init__(self, path: str) -> None:
        self.path = path

    def open_json_file(self) -> Any:
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = json.load(f)
        return self.text

    def get_json(self) -> dict:
        return ReaderJSON.open_json_file(self)
