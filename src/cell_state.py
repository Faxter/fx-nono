from enum import Enum


class CellState(Enum):
    UNKNOWN = 0
    FULL = 1
    EMPTY = 2
    MAYBE = 3
