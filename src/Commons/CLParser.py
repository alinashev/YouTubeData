import argparse
from typing import Any


class CLParser:
    def createParser(self) -> Any:
        parser = argparse.ArgumentParser()
        parser.add_argument('-v')
        return parser
