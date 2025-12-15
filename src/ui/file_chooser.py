from tkinter import Tk
from tkinter.filedialog import askopenfilename


def get_filename_from_dialog(default_dir: str):
    Tk().withdraw()
    return askopenfilename(initialdir=default_dir)
