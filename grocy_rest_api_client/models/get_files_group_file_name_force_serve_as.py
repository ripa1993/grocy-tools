from enum import Enum


class GetFilesGroupFileNameForceServeAs(str, Enum):
    PICTURE = "picture"

    def __str__(self) -> str:
        return str(self.value)
