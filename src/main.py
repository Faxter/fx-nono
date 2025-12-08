import pygame

SCREEN_BACKGROUND = "black"
GRID_WIDTH = 5
GRID_HEIGHT = 10
GRID_COLOR_RGB = (200, 200, 200)
CELL_SIZE = 50
CELL_BORDER = 1
GAME_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(SCREEN_BACKGROUND)
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(screen, GRID_COLOR_RGB, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), CELL_BORDER)
        pygame.display.flip()
        _ = clock.tick(GAME_FPS)


if __name__ == "__main__":
    main()
