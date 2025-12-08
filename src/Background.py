import pygame

GRID_COLOUR_RGB = (20, 10, 10)
CELL_BORDER = 1


class Background:
    def __init__(self, grid_height: int, grid_width: int, cell_size: int):
        self.grid_height: int = grid_height
        self.grid_width: int = grid_width
        self.grid: list = [[False for _ in range(grid_height)] for _ in range(grid_width)]
        self.cell_size: int = cell_size

    def draw_grid(self, screen: pygame.Surface):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if self.grid[x][y]:
                    pygame.draw.rect(screen, GRID_COLOUR_RGB, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(
                        screen, GRID_COLOUR_RGB, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), CELL_BORDER
                    )

    def update(self):
        left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()
        if left_pressed:
            x, y = pygame.mouse.get_pos()
            x //= self.cell_size
            y //= self.cell_size
            self.grid[x][y] = True
