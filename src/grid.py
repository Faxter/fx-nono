from src.cell_state import CellState


class Grid:
    """
    The grid is the interactive part where cells can be altered into different states.
    """

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self._grid = [[CellState.UNKNOWN for _ in range(rows)] for _ in range(columns)]

    def fill(self, x: int, y: int):
        self._grid[x][y] = CellState.FULL

    def clear(self, x: int, y: int):
        self._grid[x][y] = CellState.EMPTY

    def maybe(self, x: int, y: int):
        self._grid[x][y] = CellState.MAYBE

    def reset(self, x: int, y: int):
        self._grid[x][y] = CellState.UNKNOWN

    def is_cell_full(self, x: int, y: int):
        return self._grid[x][y] == CellState.FULL

    def is_cell_empty(self, x: int, y: int):
        return self._grid[x][y] == CellState.EMPTY

    def is_cell_maybe(self, x: int, y: int):
        return self._grid[x][y] == CellState.MAYBE

    def is_cell_unknown(self, x: int, y: int):
        return self._grid[x][y] == CellState.UNKNOWN

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
