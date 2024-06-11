from enum import Enum


class ChoreAssignmentType(str, Enum):
    IN_ALPHABETICAL_ORDER = "in-alphabetical-order"
    NO_ASSIGNMENT = "no-assignment"
    RANDOM = "random"
    WHO_LEAST_DID_FIRST = "who-least-did-first"

    def __str__(self) -> str:
        return str(self.value)
