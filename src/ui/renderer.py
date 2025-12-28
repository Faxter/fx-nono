import pygame

from src.grid import Grid, GridCoord
from src.hint import Hint
from src.puzzle import Puzzle
from src.ui.colour import Colour
from src.ui.layout import Layout

FONT = "Consolas"
WIDTH_BORDER = 1
THICK_BORDER_SPACING = 5
MENU_X_SPACING = 20
MENU = 1


class Renderer:
    def __init__(
        self,
        font_size: int,
        layout: Layout,
        cell_size: int,
    ):
        width = (layout.nonogram.puzzle.columns + layout.max_row_hints) * cell_size
        height = (layout.nonogram.puzzle.rows + layout.max_col_hints + MENU) * cell_size
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(FONT, font_size)
        self.layout = layout
        self.cell_size = cell_size

    def draw_background(self):
        self.screen.fill(Colour.BORDER)

    def draw_menu_bar(self, menus: list[str]):
        pygame.draw.rect(
            self.screen, Colour.MENU, (0, 0, self.screen.get_width(), self.cell_size)
        )
        menu_rectangles: list[pygame.Rect] = []
        x = THICK_BORDER_SPACING
        for menu_name in menus:
            text = self.font.render(menu_name, True, Colour.HINT_FONT)
            rect = text.get_rect(topleft=(x, 0))
            menu_rectangles.append(rect)
            self.screen.blit(text, rect)
            x += rect.width + MENU_X_SPACING
        if x > self.screen.get_width():
            self.screen = pygame.display.set_mode((x, self.screen.get_height()))
        return menu_rectangles

    def draw_grid(self, grid: Grid):
        for col in range(grid.columns):
            for row in range(grid.rows):
                pygame.draw.rect(
                    self.screen,
                    self.__get_cell_colour(GridCoord(col, row)),
                    self.__get_rectangle(
                        self.layout.max_row_hints + col,
                        self.layout.max_col_hints + row,
                        self.__get_border_width(col),
                        self.__get_border_width(row),
                    ),
                )

    def __get_cell_colour(self, coord: GridCoord):
        if self.layout.nonogram.grid.is_cell_full(coord):
            return Colour.FULL
        elif self.layout.nonogram.grid.is_cell_empty(coord):
            return Colour.EMPTY
        elif self.layout.nonogram.grid.is_cell_maybe(coord):
            return Colour.MAYBE
        else:
            return Colour.UNKNOWN

    def __get_rectangle(self, col: int, row: int, col_border, row_border):
        return (
            col * self.cell_size + WIDTH_BORDER,
            (row + MENU) * self.cell_size + WIDTH_BORDER,
            self.cell_size - 2 * col_border,
            self.cell_size - 2 * row_border,
        )

    def __get_border_width(self, index: int):
        return (
            WIDTH_BORDER * 2
            if (index + 1) % THICK_BORDER_SPACING == 0
            else WIDTH_BORDER
        )

    def draw_hints(self, puzzle: Puzzle):
        self.__draw_top_hints(puzzle)
        self.__draw_left_hints(puzzle)

    def __draw_top_hints(self, puzzle: Puzzle):
        for i, hints in enumerate(puzzle.column_hints):
            for j in range(self.layout.max_col_hints):
                col_border_size = self.__get_border_width(i)
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__get_rectangle(
                        self.layout.max_row_hints + i, j, col_border_size, WIDTH_BORDER
                    ),
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
                row_border_size = self.__get_border_width(i)
                rect = pygame.draw.rect(
                    self.screen,
                    Colour.HINT_BACKGROUND,
                    self.__get_rectangle(
                        j, self.layout.max_col_hints + i, WIDTH_BORDER, row_border_size
                    ),
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
            self.__get_rectangle(0, 0, 0, 0),
        )
