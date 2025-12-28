from enum import Enum

from src.grid import GridCoord
from src.ui.layout import Layout


class MouseButton(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


def get_mouse_button(index: int) -> MouseButton:
    match index:
        case 1:
            return MouseButton.LEFT
        case 2:
            return MouseButton.MIDDLE
        case 3:
            return MouseButton.RIGHT
        case _:
            return MouseButton.LEFT


MENU_ROW = 1


class MouseController:
    def __init__(self, layout: Layout, cell_size: int):
        self.layout = layout
        self.cell_size = cell_size
        self.dragging: bool = False
        self.dragged_button: MouseButton = MouseButton.LEFT
        self.dragged_cells: set[GridCoord] = set()

    def handle_mouse_down(self, button, position):
        self.dragging = True
        col, row = self.__cell_from_pos(position)
        btn: MouseButton = get_mouse_button(button)
        self.dragged_mousebutton = btn
        if self.layout.is_on_grid(col, row):
            self.__click_into_grid(col, row, btn)
        elif self.layout.is_on_top_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_top_hints(col, row)
        elif self.layout.is_on_left_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_left_hints(col, row)

    def __cell_from_pos(self, pos):
        return pos[0] // self.cell_size, pos[1] // self.cell_size

    def handle_mouse_position(self, position):
        if not self.dragging:
            return

        col, row = self.__cell_from_pos(position)
        if (
            self.layout.is_on_grid(col, row)
            and self.layout.grid_coord_from_position(col, row) not in self.dragged_cells
        ):
            self.__click_into_grid(col, row, self.dragged_mousebutton)

    def handle_mouse_up(self):
        self.dragging = False
        self.dragged_cells.clear()

    def __click_into_grid(self, col: int, row: int, button: MouseButton):
        self.completed = None
        grid_coord = self.layout.grid_coord_from_position(col, row)
        self.dragged_cells.add(grid_coord)
        left_pressed = button == MouseButton.LEFT
        middle_pressed = button == MouseButton.MIDDLE
        right_pressed = button == MouseButton.RIGHT
        if (
            (left_pressed and self.layout.nonogram.grid.is_cell_full(grid_coord))
            or (middle_pressed and self.layout.nonogram.grid.is_cell_maybe(grid_coord))
            or (right_pressed and self.layout.nonogram.grid.is_cell_empty(grid_coord))
        ):
            self.layout.nonogram.grid.reset(grid_coord)
        elif left_pressed:
            self.layout.nonogram.grid.fill(grid_coord)
        elif middle_pressed:
            self.layout.nonogram.grid.maybe(grid_coord)
        elif right_pressed:
            self.layout.nonogram.grid.clear(grid_coord)

    def __click_into_top_hints(self, col: int, row: int):
        column_hints = self.layout.nonogram.puzzle.column_hints[
            col - self.layout.max_row_hints
        ]
        no_of_empty_hint_cells = self.layout.max_col_hints - len(column_hints)
        hint_index = row - no_of_empty_hint_cells - MENU_ROW
        if hint_index >= 0:
            hint = column_hints[hint_index]
            hint.toggle_crossed()

    def __click_into_left_hints(self, col: int, row: int):
        row_hints = self.layout.nonogram.puzzle.row_hints[
            row - self.layout.max_col_hints - MENU_ROW
        ]
        no_of_empty_hint_cells = self.layout.max_row_hints - len(row_hints)
        hint_index = col - no_of_empty_hint_cells
        if hint_index >= 0:
            hint = row_hints[col - no_of_empty_hint_cells]
            hint.toggle_crossed()
