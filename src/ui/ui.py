from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

from src.grid import GridCoord
from src.nonogram import Nonogram
from src.ui.layout import Layout
from src.ui.mouse_button import MouseButton, get_mouse_button
from src.ui.renderer import Renderer

WINDOW_TITLE = "fx-nono"
GAME_FPS = 60


class Ui:
    def __init__(self, nonogram: Nonogram, cell_size: int, font_size: int):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.nonogram = nonogram
        self.cell_size: int = cell_size
        self.clock = pygame.time.Clock()
        self.max_row_hints = max(list(map(len, nonogram.puzzle.row_hints)))
        self.max_col_hints = max(list(map(len, nonogram.puzzle.column_hints)))
        self.layout = Layout(nonogram, self.max_row_hints, self.max_col_hints)
        self.renderer = Renderer(font_size, self.layout, cell_size)
        self.running = True
        self.completed: None | bool = None
        self.dragging = False
        self.dragged_mousebutton = MouseButton.LEFT
        self.dragged_cells: set[GridCoord] = set()

    def run(self):
        while self.running:
            self.renderer.draw_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.completed:
                    self.__handle_click(event.button, event.pos)
                elif event.type == pygame.MOUSEMOTION and self.dragging:
                    self.__handle_mouse_position(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.__handle_un_click()
                    self.__check_complete()
            self.renderer.draw_hints(self.nonogram.puzzle)
            self.renderer.draw_grid(self.nonogram.grid)
            self.renderer.draw_success_indicator(self.completed)
            pygame.display.flip()
            _ = self.clock.tick(GAME_FPS)
        pygame.quit()

    def __handle_click(self, button, position):
        self.dragging = True
        col = position[0] // self.cell_size
        row = position[1] // self.cell_size
        btn: MouseButton = get_mouse_button(button)
        self.dragged_mousebutton = btn
        if self.layout.is_on_grid(col, row):
            self.__click_into_grid(col, row, btn)
        elif self.layout.is_on_top_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_top_hints(col, row)
        elif self.layout.is_on_left_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_left_hints(col, row)

    def __handle_mouse_position(self, position):
        col = position[0] // self.cell_size
        row = position[1] // self.cell_size
        if (
            self.layout.is_on_grid(col, row)
            and self.layout.grid_coord_from_position(col, row) not in self.dragged_cells
        ):
            self.__click_into_grid(col, row, self.dragged_mousebutton)

    def __handle_un_click(self):
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
            (left_pressed and self.nonogram.grid.is_cell_full(grid_coord))
            or (middle_pressed and self.nonogram.grid.is_cell_maybe(grid_coord))
            or (right_pressed and self.nonogram.grid.is_cell_empty(grid_coord))
        ):
            self.nonogram.grid.reset(grid_coord)
        elif left_pressed:
            self.nonogram.grid.fill(grid_coord)
        elif middle_pressed:
            self.nonogram.grid.maybe(grid_coord)
        elif right_pressed:
            self.nonogram.grid.clear(grid_coord)

    def __click_into_top_hints(self, col: int, row: int):
        column_hints = self.nonogram.puzzle.column_hints[col - self.max_row_hints]
        no_of_empty_hint_cells = self.max_col_hints - len(column_hints)
        hint_index = row - no_of_empty_hint_cells
        if hint_index >= 0:
            hint = column_hints[hint_index]
            hint.toggle_crossed()

    def __click_into_left_hints(self, col: int, row: int):
        row_hints = self.nonogram.puzzle.row_hints[row - self.max_col_hints]
        no_of_empty_hint_cells = self.max_row_hints - len(row_hints)
        hint_index = col - no_of_empty_hint_cells
        if hint_index >= 0:
            hint = row_hints[col - no_of_empty_hint_cells]
            hint.toggle_crossed()

    def __check_complete(self):
        if self.nonogram.grid.is_complete():
            self.completed = self.nonogram.verify()
