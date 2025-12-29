from src.file_parser import load_savefile, write_savefile
from src.nonogram import Nonogram


class Menu:
    def __init__(self, nonogram: Nonogram):
        self.menu_items = {
            "Open": Menu.open,
            "Save": Menu.save,
            "Load": Menu.load,
            "About": Menu.about,
        }
        self.nonogram = nonogram

    def menu_names(self):
        return list(self.menu_items.keys())

    def select_menu(self, menu: str):
        if menu in self.menu_items:
            self.menu_items[menu](self)

    def save(self):
        write_savefile("test", self.nonogram.grid)

    def open(self):
        print("open")

    def load(self):
        new_grid = load_savefile("test")
        self.nonogram.set_grid(new_grid)

    def about(self):
        print("fx-nono")
