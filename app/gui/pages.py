import tkinter as tk


class Page(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def on_shown(self):
        pass


class PageContainerFrame(tk.Frame):
    def __init__(self, master, page_classes, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.pages = {}

        self.grid(column=0, row=0, sticky=tk.NSEW)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for page_class in page_classes:
            page_name = page_class.__name__
            page = page_class(self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky=tk.NSEW)

        if len(page_classes):
            self.show_page(page_classes[0].__name__)

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()
        page.on_shown()
        return page
