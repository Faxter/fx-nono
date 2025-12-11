from src.hint import create_hints


class Puzzle:
    def __init__(
        self,
        rows: int,
        columns: int,
        row_hints: list[list[int]],
        column_hints: list[list[int]],
    ):
        """example of a small valid nonogram:
        {
            "rows": 8,
            "columns": 5,
            "row_hints": [[3], [1, 1], [1, 1, 1], [3], [3], [3], [1]]
            "column_hints": [[3], [1, 3], [1, 6], [1, 3], [3]]
        }
        """
        if rows <= 0:
            raise ValueError("number of rows must be greater than zero")
        if columns <= 0:
            raise ValueError("number of columns must be greater than zero")
        if len(row_hints) != rows:
            raise ValueError("number of row hints does not match number of rows")
        if len(column_hints) != columns:
            raise ValueError("number of column hints does not match number of columns")
        self.rows = rows
        self.columns = columns
        self.row_hints = create_hints(row_hints)
        self.column_hints = create_hints(column_hints)
