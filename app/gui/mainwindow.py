import tkinter as tk

from app.gui import look, utils
from app.gui.pages import PageContainerFrame
from app.gui.pages.mainmenu import MainMenuPage
from app.gui.pages.selectbuyer import SelectBuyerPage
from app.gui.pages.newinvoice import NewInvoicePage


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("desktop-inv v-0.1")
        utils.set_window_icon(self, "icon.png")
        self.minsize(1200, 800)
        utils.center_window(self)

        pages = [MainMenuPage, SelectBuyerPage, NewInvoicePage]
        self.page_container = PageContainerFrame(self, pages, **look.frame)
        self.page_container.pack(fill=tk.BOTH, expand=True)

        self.bind("<Escape>", lambda _: self.page_container.pop_page())
