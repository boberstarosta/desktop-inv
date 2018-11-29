import tkinter as tk
from app.gui import look


class Page(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def on_hidden(self):
        pass

    def on_shown(self, *args, **kwargs):
        pass


class PageContainerFrame(tk.Frame):
    def __init__(self, master, page_classes, **kwargs):
        super().__init__(master, **kwargs)

        self.pages = {}
        self.stack = []
        self.current_page = None
        self.last_page = None

        self.grid(column=0, row=0, sticky=tk.NSEW)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for page_class in page_classes:
            page_name = page_class.__name__
            page = page_class(self, **look.frame)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky=tk.NSEW)

        if page_classes:
            self.push_page(page_classes[0].__name__)

    def push_page(self, page_name, *args, **kwargs):
        page = self.pages[page_name]
        if self.stack:
            self.stack[-1].on_hidden()
        page.tkraise()
        page.on_shown(*args, **kwargs)
        self.stack.append(page)
        return page

    def pop_page(self, *args, **kwargs):
        if len(self.stack) <= 1:
            return
        self.stack.pop().on_hidden()
        page = self.stack[-1]
        page.tkraise()
        page.on_shown(*args, **kwargs)
        return page

    def change_page(self, page_name, *args, **kwargs):
        self.stack.pop().on_hidden()
        page = self.pages[page_name]
        page.tkraise()
        page.on_shown(*args, **kwargs)
        self.stack.append(page)
        return page
