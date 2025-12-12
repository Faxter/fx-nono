from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

from src.colour import Colour
from src.hint import Hint
from src.mouse_button import MouseButton, get_mouse_button
from src.nonogram import Nonogram

WINDOW_TITLE = "fx-nono"
WIDTH_BORDER = 1
GAME_FPS = 60
FONT = "Consolas"


class Ui:
    def __init__(self, nonogram: Nonogram, cell_size: int, font_size: int):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.nonogram = nonogram
        self.cell_size: int = cell_size
        self.font = pygame.font.SysFont(FONT, font_size)
        self.clock = pygame.time.Clock()
        self.max_row_hints = max(list(map(len, nonogram.puzzle.row_hints)))
        self.max_col_hints = max(list(map(len, nonogram.puzzle.column_hints)))
        width = (nonogram.puzzle.columns + self.max_row_hints) * self.cell_size
        height = (nonogram.puzzle.rows + self.max_col_hints) * self.cell_size
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.completed: None | bool = None

    def run(self):
        while self.running:
            self.screen.fill(Colour.BORDER)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP and not self.completed:
                    self.__handle_click(event.button, event.pos)
                    self.__check_complete()
            self.__draw_hints()
            self.__draw_grid()
            self.__draw_success_indicator()
            pygame.display.flip()
            _ = self.clock.tick(GAME_FPS)
        pygame.quit()

    def __handle_click(self, button, position):
        col = position[0] // self.cell_size
        row = position[1] // self.cell_size
        btn: MouseButton = get_mouse_button(button)
        if self.__is_click_event_on_grid(col, row):
            self.__click_into_grid(col, row, btn)
        elif self.__is_click_event_on_top_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_top_hints(col, row)
        elif self.__is_click_event_on_left_hint(col, row) and btn == MouseButton.LEFT:
            self.__click_into_left_hints(col, row)

    def __is_click_event_on_grid(self, col: int, row: int):
        return (
            col >= self.max_row_hints
            and col <= self.max_row_hints + self.nonogram.grid.columns
            and row >= self.max_col_hints
            and row <= self.max_col_hints + self.nonogram.grid.rows
        )

    def __is_click_event_on_top_hint(self, col: int, row: int):
        return (
            row >= 0
            and row < self.max_col_hints
            and col >= self.max_row_hints
            and col < self.max_row_hints + self.nonogram.puzzle.columns
        )

    def __is_click_event_on_left_hint(self, col: int, row: int):
        return (
            col >= 0
            and col < self.max_row_hints
            and row >= self.max_col_hints
            and row < self.max_col_hints + self.nonogram.puzzle.rows
        )

    def __click_into_grid(self, col: int, row: int, button: MouseButton):
        self.completed = None
        grid_col, grid_row = self.__grid_coord_from_position(col, row)
        left_pressed = button == MouseButton.LEFT
        middle_pressed = button == MouseButton.MIDDLE
        right_pressed = button == MouseButton.RIGHT
        if (
            (left_pressed and self.nonogram.grid.is_cell_full(grid_col, grid_row))
            or (middle_pressed and self.nonogram.grid.is_cell_maybe(grid_col, grid_row))
            or (right_pressed and self.nonogram.grid.is_cell_empty(grid_col, grid_row))
        ):
            self.nonogram.grid.reset(grid_col, grid_row)
        elif left_pressed:
            self.nonogram.grid.fill(grid_col, grid_row)
        elif middle_pressed:
            self.nonogram.grid.maybe(grid_col, grid_row)
        elif right_pressed:
            self.nonogram.grid.clear(grid_col, grid_row)

    def __grid_coord_from_position(self, col: int, row: int):
        col -= self.max_row_hints
        row -= self.max_col_hints
        return col, row

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

    def __draw_grid(self):
        grid = self.nonogram.grid
        for col in range(grid.columns):
            for row in range(grid.rows):
                colour = ()
                if grid.is_cell_full(col, row):
                    colour = Colour.FULL
                elif grid.is_cell_empty(col, row):
                    colour = Colour.EMPTY
                elif grid.is_cell_maybe(col, row):
                    colour = Colour.MAYBE
                else:
                    colour = Colour.UNKNOWN
                pygame.draw.rect(
                    self.screen,
                    colour,
                    self.__grid_rect(
                        self.max_row_hints + col, self.max_col_hints + row
                    ),
                )

    def __grid_rect(self, col: int, row: int):
        return (
            col * self.cell_size + WIDTH_BORDER,
            row * self.cell_size + WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
        )

    def __draw_hints(self):
        self.__draw_top_hints()
        self.__draw_left_hints()

    def __draw_top_hints(self):
        for i in range(self.nonogram.grid.columns):
            for j in range(self.max_col_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__grid_rect(self.max_row_hints + i, j),
                )
                self.__fill_with_hint(
                    rect,
                    j,
                    self.nonogram.puzzle.column_hints[i],
                    self.max_col_hints,
                )

    def __draw_left_hints(self):
        for i in range(self.nonogram.grid.rows):
            for j in range(self.max_row_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__grid_rect(j, self.max_col_hints + i),
                )
                self.__fill_with_hint(
                    rect,
                    j,
                    self.nonogram.puzzle.row_hints[i],
                    self.max_row_hints,
                )

    def __fill_with_hint(
        self,
        rect: pygame.Rect,
        hint_index: int,
        hints: list[Hint],
        max_amount_of_hints: int,
    ):
        no_of_empty_hint_cells = max_amount_of_hints - len(hints)
        if hint_index - no_of_empty_hint_cells >= 0:
            hint = hints[hint_index - no_of_empty_hint_cells]
            hint_text = str(hint.value)
            self.font.strikethrough = hint.crossed
            text_surface = self.font.render(hint_text, True, Colour.HINT_FONT)
            rect_alignment = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, rect_alignment)

    def __draw_success_indicator(self):
        if self.completed is None:
            return
        pygame.draw.rect(
            self.screen,
            Colour.SUCCESS if self.completed else Colour.FAILURE,
            self.__grid_rect(0, 0),
        )
