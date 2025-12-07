import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        _ = clock.tick(60)


if __name__ == "__main__":
    main()
