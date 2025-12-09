from dataclasses import dataclass


@dataclass
class Puzzle:
    rows: int
    columns: int


# TODO: add hints here as lists of ints


def parse_puzzle(puzzle: dict) -> Puzzle:
    """Expected structure:
    {
        "rows": 5,
        "columns": 10,
    }
    """
    return Puzzle(rows=puzzle["rows"], columns=puzzle["columns"])
