from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def get_filepath_from_dialog(default_dir: str = Path.home().as_posix()):
    Tk().withdraw()
    try:
        return Path(askopenfilename(initialdir=default_dir))
    except TypeError:
        return Path()


def get_filepath_to_save_as_from_dialog(default_dir: str = Path.home().as_posix()):
    Tk().withdraw()
    try:
        return Path(asksaveasfilename(initialdir=default_dir))
    except TypeError:
        return Path()
