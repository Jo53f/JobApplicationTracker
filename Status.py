from enum import auto, Enum


class Status(Enum):
    """
    Enum for status of job application.

    Methods
    -------
    label(self) -> str
        returns the label of the status
    """
    APPLIED = 1
    REJECTED = 2
    ACCEPTED = 3

    def label(self) -> str:
        return self.name.lower()
