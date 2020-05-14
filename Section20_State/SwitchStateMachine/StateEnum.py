from enum import Enum, auto


class StateEnum(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()
