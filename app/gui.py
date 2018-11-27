import tkinter as tk

from app import guiutils


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("desktop-inv v-0.1")
        guiutils.set_window_icon(self, "icon.png")
        self.minsize(600, 600)
        guiutils.center_window(self)
