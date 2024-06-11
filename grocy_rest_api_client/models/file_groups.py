from enum import Enum


class FileGroups(str, Enum):
    EQUIPMENTMANUALS = "equipmentmanuals"
    PRODUCTPICTURES = "productpictures"
    RECIPEPICTURES = "recipepictures"
    USERFILES = "userfiles"
    USERPICTURES = "userpictures"

    def __str__(self) -> str:
        return str(self.value)
