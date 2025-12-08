import pygame

from src.CellState import CellState

COLOUR_BORDER = (0, 0, 0)
COLOUR_UNKNOWN = (130, 133, 130)
COLOUR_FULL = (56, 53, 53)
COLOUR_EMPTY = (210, 213, 210)
COLOUR_MAYBE = (220, 30, 170)
WIDTH_BORDER = 1


class Background:
    def __init__(self, grid_height: int, grid_width: int, cell_size: int):
        self.grid_height: int = grid_height
        self.grid_width: int = grid_width
        self.grid: list = [[CellState.UNKNOWN for _ in range(grid_height)] for _ in range(grid_width)]
        self.cell_size: int = cell_size

    def draw_grid(self, screen: pygame.Surface):
        screen.fill(COLOUR_BORDER)
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                colour = ()
                if self.grid[x][y] == CellState.FULL:
                    colour = COLOUR_FULL
                elif self.grid[x][y] == CellState.EMPTY:
                    colour = COLOUR_EMPTY
                elif self.grid[x][y] == CellState.MAYBE:
                    colour = COLOUR_MAYBE
                else:
                    colour = COLOUR_UNKNOWN
                pygame.draw.rect(screen, colour, self.__grid_rect(x, y))

    def __grid_rect(self, x: int, y: int):
        return (
            x * self.cell_size + WIDTH_BORDER,
            y * self.cell_size + WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
            self.cell_size - 2 * WIDTH_BORDER,
        )

    def update(self):
        for event in pygame.event.get(pygame.MOUSEBUTTONUP):
            left_pressed = event.button == 1
            middle_pressed = event.button == 2
            right_pressed = event.button == 3
            x, y = (event.pos[0] // self.cell_size, event.pos[1] // self.cell_size)

            if (
                (left_pressed and self.grid[x][y] == CellState.FULL)
                or (middle_pressed and self.grid[x][y] == CellState.MAYBE)
                or (right_pressed and self.grid[x][y] == CellState.EMPTY)
            ):
                self.grid[x][y] = CellState.UNKNOWN
            elif left_pressed:
                self.grid[x][y] = CellState.FULL
            elif middle_pressed:
                self.grid[x][y] = CellState.MAYBE
            elif right_pressed:
                self.grid[x][y] = CellState.EMPTY
