import tkinter as tk

from . import utils


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("desktop-inv v-0.1")
        utils.set_window_icon(self, "icon.png")
        self.minsize(600, 600)
        utils.center_window(self)
