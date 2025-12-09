import pygame

from src.nonogram import Nonogram

COLOUR_BORDER = (0, 0, 0)
COLOUR_UNKNOWN = (130, 133, 130)
COLOUR_FULL = (56, 53, 53)
COLOUR_EMPTY = (210, 213, 210)
COLOUR_MAYBE = (220, 30, 170)
WIDTH_BORDER = 1
GAME_FPS = 60


class Ui:
    def __init__(self, nonogram: Nonogram, cell_size: int):
        pygame.init()
        pygame.display.set_caption("fx-nono")
        self.nonogram = nonogram
        self.cell_size: int = cell_size
        self.clock = pygame.time.Clock()

        width = nonogram.puzzle.columns * self.cell_size
        height = nonogram.puzzle.rows * self.cell_size
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
        col = x // self.cell_size
        row = y // self.cell_size
        col = max(0, col)
        row = max(0, row)
        col = min(col, self.nonogram.grid.columns - 1)
        row = min(row, self.nonogram.grid.rows - 1)
        return col, row

    def draw_grid(self):
        grid = self.nonogram.grid
        for x in range(grid.columns):
            for y in range(grid.rows):
                colour = ()
                if grid.is_cell_full(x, y):
                    colour = COLOUR_FULL
                elif grid.is_cell_empty(x, y):
                    colour = COLOUR_EMPTY
                elif grid.is_cell_maybe(x, y):
                    colour = COLOUR_MAYBE
                else:
                    colour = COLOUR_UNKNOWN
                pygame.draw.rect(self.screen, colour, self.__grid_rect(x, y))

    def __grid_rect(self, x: int, y: int):
        return (
            x * self.cell_size + WIDTH_BORDER,
            y * self.cell_size + WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
        )
