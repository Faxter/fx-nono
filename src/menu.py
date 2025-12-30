from src.file_parser import load_savefile, write_savefile
from src.nonogram import Nonogram
from src.ui.file_chooser import (
    get_filepath_from_dialog,
    get_filepath_to_save_as_from_dialog,
)


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
        filepath = get_filepath_to_save_as_from_dialog()
        write_savefile(filepath, self.nonogram.grid)

    def open(self):
        print("open")

    def load(self):
        filepath = get_filepath_from_dialog()
        new_grid = load_savefile(filepath)
        if new_grid is None:
            pass
        elif self.nonogram.is_compatible(new_grid):
            self.nonogram.set_grid(new_grid)
        else:
            print("save file is not compatible with puzzle size")

    def about(self):
        print("fx-nono")
