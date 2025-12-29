from src.grid import GridCoord
from src.nonogram import Nonogram

MENU_ROW = 1


class Layout:
    def __init__(self, nonogram: Nonogram):
        self.nonogram = nonogram
        self.max_row_hints = max(list(map(len, nonogram.puzzle.row_hints)))
        self.max_col_hints = max(list(map(len, nonogram.puzzle.column_hints)))

    def grid_coord_from_position(self, col: int, row: int):
        col -= self.max_row_hints
        row -= self.max_col_hints + MENU_ROW
        return GridCoord(col, row)

    def is_on_grid(self, col: int, row: int):
        return (
            col >= self.max_row_hints
            and col < self.max_row_hints + self.nonogram.grid.columns
            and row >= self.max_col_hints + MENU_ROW
            and row < self.max_col_hints + self.nonogram.grid.rows + MENU_ROW
        )

    def is_on_top_hint(self, col: int, row: int):
        return (
            row >= MENU_ROW
            and row < self.max_col_hints + MENU_ROW
            and col >= self.max_row_hints
            and col < self.max_row_hints + self.nonogram.puzzle.columns
        )

    def is_on_left_hint(self, col: int, row: int):
        return (
            col >= 0
            and col < self.max_row_hints
            and row >= self.max_col_hints + MENU_ROW
            and row < self.max_col_hints + self.nonogram.puzzle.rows + MENU_ROW
        )

    def is_on_menu_bar(self, row: int):
        return row == 0
