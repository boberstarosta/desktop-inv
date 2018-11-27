import tkinter as tk
from app.threads import ClockThread


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


class MainMenuPage(Page):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.var_time = tk.StringVar()
        clock_label = tk.Label(self, textvariable=self.var_time,
                               font=("TkFixedFont", 20, "bold"), fg="#777")
        clock_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.clock_thread = ClockThread(self.update_clock)
        self.clock_thread.start()

        btn_new = tk.Button(self, text="Nowa faktura",
                            font=("TkFixedFont", 20, "bold"),
                            command=self.new_invoice)
        btn_new.pack(fill=tk.BOTH, expand=True)

    def update_clock(self, time):
        self.var_time.set(time)

    def new_invoice(self):
        pass
