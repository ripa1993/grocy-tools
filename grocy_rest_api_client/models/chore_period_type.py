from enum import Enum


class ChorePeriodType(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    MANUALLY = "manually"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
