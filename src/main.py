import pygame

SCREEN_BACKGROUND = (233, 240, 233)
GRID_WIDTH = 5
GRID_HEIGHT = 10
GRID_COLOR_RGB = (20, 10, 10)
CELL_SIZE = 50
CELL_BORDER = 1
GAME_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    clock = pygame.time.Clock()
    grid = [[False for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
    while True:
        screen.fill(SCREEN_BACKGROUND)
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if grid[x][y]:
                    pygame.draw.rect(screen, GRID_COLOR_RGB, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(screen, GRID_COLOR_RGB, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), CELL_BORDER)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = (event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE)
                grid[x][y] = True
        pygame.display.flip()
        _ = clock.tick(GAME_FPS)


if __name__ == "__main__":
    main()
