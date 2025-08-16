from enum import auto, Enum


class Status(Enum):
    APPLIED = 1
    REJECTED = 2
    ACCEPTED = 3

    def label(self):
        return self.name.lower()
