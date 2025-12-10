import pygame

from src.nonogram import Nonogram

COLOUR_BORDER = (0, 0, 0)
COLOUR_UNKNOWN = (130, 133, 130)
COLOUR_FULL = (56, 53, 53)
COLOUR_EMPTY = (210, 213, 210)
COLOUR_MAYBE = (220, 30, 170)
COLOUR_HINT_BACKGROUND = (80, 83, 80)
COLOUR_HINT_FONT = (255, 255, 255)
WIDTH_BORDER = 1
GAME_FPS = 60


class Ui:
    def __init__(self, nonogram: Nonogram, cell_size: int, font_size: int):
        pygame.init()
        pygame.display.set_caption("fx-nono")
        self.nonogram = nonogram
        self.cell_size: int = cell_size
        self.font = pygame.font.SysFont("Consolas", font_size)
        self.clock = pygame.time.Clock()

        self.max_row_hints = max(list(map(len, nonogram.puzzle.row_hints)))
        self.max_col_hints = max(list(map(len, nonogram.puzzle.column_hints)))
        width = (nonogram.puzzle.columns + self.max_row_hints) * self.cell_size
        height = (nonogram.puzzle.rows + self.max_col_hints) * self.cell_size
        self.screen = pygame.display.set_mode((width, height))

        self.running = True

    def run(self):
        while self.running:
            self.screen.fill(COLOUR_BORDER)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.__handle_click(event.button, event.pos)
            self.draw_hints()
            self.draw_grid()
            pygame.display.flip()
            _ = self.clock.tick(GAME_FPS)
        pygame.quit()

    def __handle_click(self, button, position):
        col, row = self.__cell_coord_from_position(position)
        left_pressed = button == 1
        middle_pressed = button == 2
        right_pressed = button == 3

        if (
            (left_pressed and self.nonogram.grid.is_cell_full(col, row))
            or (middle_pressed and self.nonogram.grid.is_cell_maybe(col, row))
            or (right_pressed and self.nonogram.grid.is_cell_empty(col, row))
        ):
            self.nonogram.grid.reset(col, row)
        elif left_pressed:
            self.nonogram.grid.fill(col, row)
        elif middle_pressed:
            self.nonogram.grid.maybe(col, row)
        elif right_pressed:
            self.nonogram.grid.clear(col, row)

    def __cell_coord_from_position(self, position):
        x, y = position
        col = x // self.cell_size - self.max_row_hints
        row = y // self.cell_size - self.max_col_hints
        col = max(0, col)
        row = max(0, row)
        col = min(col, self.nonogram.grid.columns - 1)
        row = min(row, self.nonogram.grid.rows - 1)
        return col, row

    def draw_grid(self):
        grid = self.nonogram.grid
        for col in range(grid.columns):
            for row in range(grid.rows):
                colour = ()
                if grid.is_cell_full(col, row):
                    colour = COLOUR_FULL
                elif grid.is_cell_empty(col, row):
                    colour = COLOUR_EMPTY
                elif grid.is_cell_maybe(col, row):
                    colour = COLOUR_MAYBE
                else:
                    colour = COLOUR_UNKNOWN
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

    def draw_hints(self):
        for i in range(self.nonogram.grid.columns):
            for j in range(self.max_col_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    COLOUR_HINT_BACKGROUND,
                    self.__grid_rect(self.max_row_hints + i, j),
                )
                column_hints = self.nonogram.puzzle.column_hints[i]
                no_of_empty_hint_cells = self.max_col_hints - len(column_hints)
                if j - no_of_empty_hint_cells >= 0:
                    hint_text = str(column_hints[j - no_of_empty_hint_cells])
                    text_surface = self.font.render(hint_text, True, COLOUR_HINT_FONT)
                    rect_alignment = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, rect_alignment)

        for i in range(self.nonogram.grid.rows):
            for j in range(self.max_row_hints):
                rect = pygame.draw.rect(
                    self.screen,
                    COLOUR_HINT_BACKGROUND,
                    self.__grid_rect(j, self.max_col_hints + i),
                )
                row_hints = self.nonogram.puzzle.row_hints[i]
                no_of_empty_hint_cells = self.max_row_hints - len(row_hints)
                if j - no_of_empty_hint_cells >= 0:
                    hint_text = str(row_hints[j - no_of_empty_hint_cells])
                    text_surface = self.font.render(hint_text, True, COLOUR_HINT_FONT)
                    rect_alignment = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, rect_alignment)
