import pygame

from src.grid import Grid, GridCoord
from src.hint import Hint
from src.puzzle import Puzzle
from src.ui.colour import Colour
from src.ui.layout import Layout

FONT = "Consolas"
WIDTH_BORDER = 1


class Renderer:
    def __init__(
        self,
        font_size: int,
        layout: Layout,
        cell_size: int,
    ):
        width = (layout.nonogram.puzzle.columns + layout.max_row_hints) * cell_size
        height = (layout.nonogram.puzzle.rows + layout.max_col_hints) * cell_size
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(FONT, font_size)
        self.layout = layout
        self.cell_size = cell_size

    def draw_background(self):
        self.screen.fill(Colour.BORDER)

    def draw_grid(self, grid: Grid):
        for col in range(grid.columns):
            for row in range(grid.rows):
                colour = ()
                coord = GridCoord(col, row)
                if grid.is_cell_full(coord):
                    colour = Colour.FULL
                elif grid.is_cell_empty(coord):
                    colour = Colour.EMPTY
                elif grid.is_cell_maybe(coord):
                    colour = Colour.MAYBE
                else:
                    colour = Colour.UNKNOWN
                pygame.draw.rect(
                    self.screen,
                    colour,
                    self.__grid_rect(
                        self.layout.max_row_hints + col, self.layout.max_col_hints + row
                    ),
                )

    def __grid_rect(self, col: int, row: int):
        return (
            col * self.cell_size + WIDTH_BORDER,
            row * self.cell_size + WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
        )

    def draw_hints(self, puzzle: Puzzle):
        self.__draw_top_hints(puzzle)
        self.__draw_left_hints(puzzle)

    def __draw_top_hints(self, puzzle: Puzzle):
        for i, hints in enumerate(puzzle.column_hints):
            for j in range(self.layout.max_col_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__grid_rect(self.layout.max_row_hints + i, j),
                )
                self.__fill_with_hint(
                    rect,
                    j,
                    hints,
                    self.layout.max_col_hints,
                )

    def __draw_left_hints(self, puzzle: Puzzle):
        for i, hints in enumerate(puzzle.row_hints):
            for j in range(self.layout.max_row_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__grid_rect(j, self.layout.max_col_hints + i),
                )
                self.__fill_with_hint(
                    rect,
                    j,
                    hints,
                    self.layout.max_row_hints,
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

    def draw_success_indicator(self, completed: None | bool):
        if completed is None:
            return
        pygame.draw.rect(
            self.screen,
            Colour.SUCCESS if completed else Colour.FAILURE,
            self.__grid_rect(0, 0),
        )
