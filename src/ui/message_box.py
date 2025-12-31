from tkinter import Tk, messagebox


def show_message(title: str, header: str, msg: str):
    messagebox.showinfo(title, header, detail=msg)
    Tk().withdraw()
