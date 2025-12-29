class Menu:
    def __init__(self):
        self.menu_items = {"Open": open, "Save": save, "Load": load, "About": about}

    def menu_names(self):
        return list(self.menu_items.keys())

    def select_menu(self, menu: str):
        if menu in self.menu_items:
            self.menu_items[menu]()


def open():
    print("open")


def save():
    print("save")


def load():
    print("load")


def about():
    print("fx-nono")
