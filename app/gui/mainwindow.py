import tkinter as tk

from . import utils
from .pages import PageContainerFrame, MainMenuPage, SelectCustomerPage


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("desktop-inv v-0.1")
        utils.set_window_icon(self, "icon.png")
        self.minsize(1200, 800)
        utils.center_window(self)

        pages = [MainMenuPage, SelectCustomerPage]
        page_container = PageContainerFrame(self, pages)
        page_container.pack(fill=tk.BOTH, expand=True)
