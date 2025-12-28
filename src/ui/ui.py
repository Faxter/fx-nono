from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

from src.nonogram import Nonogram
from src.ui.layout import Layout
from src.ui.mouse import MouseController
from src.ui.renderer import Renderer

WINDOW_TITLE = "fx-nono"
GAME_FPS = 60


class Ui:
    def __init__(self, nonogram: Nonogram, cell_size: int, font_size: int):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.nonogram = nonogram
        self.clock = pygame.time.Clock()
        self.layout = Layout(nonogram)
        self.renderer = Renderer(font_size, self.layout, cell_size)
        self.mouse = MouseController(self.layout, cell_size)
        self.running = True
        self.completed: None | bool = None

    def run(self):
        while self.running:
            self.renderer.draw_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.completed:
                    self.mouse.handle_mouse_down(event.button, event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse.handle_mouse_position(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse.handle_mouse_up()
                    self.__check_complete()
            self.renderer.draw_hints(self.nonogram.puzzle)
            self.renderer.draw_grid(self.nonogram.grid)
            self.renderer.draw_success_indicator(self.completed)
            self.renderer.draw_menu_bar()
            pygame.display.flip()
            _ = self.clock.tick(GAME_FPS)
        pygame.quit()

    def __check_complete(self):
        if self.nonogram.grid.is_complete():
            self.completed = self.nonogram.verify()
        else:
            self.completed = None
