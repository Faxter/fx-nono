from src.cell_state import CellState


class GridCoord:
    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row

    def __repr__(self):
        return f"{self.column}:{self.row}"

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __hash__(self):
        return hash((self.column, self.row))


class Grid:
    """
    The grid is the interactive part where cells can be altered into different states.
    """

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self._grid = [[CellState.UNKNOWN for _ in range(rows)] for _ in range(columns)]

    def fill(self, coord: GridCoord):
        self._grid[coord.column][coord.row] = CellState.FULL

    def clear(self, coord: GridCoord):
        self._grid[coord.column][coord.row] = CellState.EMPTY

    def maybe(self, coord: GridCoord):
        self._grid[coord.column][coord.row] = CellState.MAYBE

    def reset(self, coord: GridCoord):
        self._grid[coord.column][coord.row] = CellState.UNKNOWN

    def is_cell_full(self, coord: GridCoord):
        return self._grid[coord.column][coord.row] == CellState.FULL

    def is_cell_empty(self, coord: GridCoord):
        return self._grid[coord.column][coord.row] == CellState.EMPTY

    def is_cell_maybe(self, coord: GridCoord):
        return self._grid[coord.column][coord.row] == CellState.MAYBE

    def is_cell_unknown(self, coord: GridCoord):
        return self._grid[coord.column][coord.row] == CellState.UNKNOWN

    def get_row(self, index: int):
        return [self._grid[column][index] for column in range(self.columns)]

    def get_column(self, index: int):
        return self._grid[index]

    def is_complete(self):
        for c in range(self.columns):
            for cell in self.get_column(c):
                if cell != CellState.FULL and cell != CellState.EMPTY:
                    return False
        return True
