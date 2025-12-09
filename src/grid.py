from src.cell_state import CellState


class Grid:
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
