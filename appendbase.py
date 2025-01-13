# an append-only database made with json
# is this google hyper-scaleable? no
# do i care? no

import json
from typing import Any

class Appendbase:
    stuff: list[Any]

    def __init__(self, stuff: list[Any]):
        self.stuff = stuff

    def append(self, thing: Any):
        self.stuff.append(thing)

    @classmethod
    def from_file(cls, filename: str):
        try:
            with open(filename, "r") as file:
                stuff = json.loads(file.read())
        except FileNotFoundError:
            return cls([])
        return cls(stuff)

    def to_file(self, filename: str):
        with open(filename, "w+") as file:
            file.write(json.dumps(self.stuff))
