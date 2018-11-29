import tkinter as tk


class Page(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def on_hidden(self):
        pass

    def on_shown(self, *args, **kwargs):
        pass


class PageContainerFrame(tk.Frame):
    def __init__(self, master, page_classes, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.pages = {}
        self.current_page = None

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

    def show_page(self, page_name, *args, **kwargs):
        page = self.pages[page_name]
        if self.current_page is not None:
            self.current_page.on_hidden()
        page.tkraise()
        page.on_shown(*args, **kwargs)
        self.current_page = page
        return page

