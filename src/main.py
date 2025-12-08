import pygame

from src.Background import Background

COLOUR_GRID = (0, 0, 0)
GRID_WIDTH = 5
GRID_HEIGHT = 10
CELL_SIZE = 50
CELL_BORDER = 1
GAME_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    clock = pygame.time.Clock()
    background: Background = Background(GRID_HEIGHT, GRID_WIDTH, CELL_SIZE)

    while True:
        for event in pygame.event.get(exclude=pygame.MOUSEBUTTONUP):
            if event.type == pygame.QUIT:
                return

        screen.fill(COLOUR_GRID)
        background.update()
        background.draw_grid(screen)
        pygame.display.flip()
        _ = clock.tick(GAME_FPS)


if __name__ == "__main__":
    main()
