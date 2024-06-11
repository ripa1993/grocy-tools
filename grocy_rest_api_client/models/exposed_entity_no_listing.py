from enum import Enum


class ExposedEntityNoListing(str, Enum):
    API_KEYS = "api_keys"

    def __str__(self) -> str:
        return str(self.value)
