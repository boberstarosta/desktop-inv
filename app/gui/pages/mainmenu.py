import tkinter as tk
from app.threads import ClockThread
from app.gui.pages import Page
from app.gui import look


class MainMenuPage(Page):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        frame = tk.Frame(self, look.frame_inv)
        frame.pack(side=tk.TOP, fill=tk.BOTH)

        heading_label = tk.Label(frame, text="desktop-inv v-0.1",
                                 **look.label_inv)
        heading_label.pack(side=tk.TOP, fill=tk.X, expand=True, **look.pack)

        self.var_time = tk.StringVar()
        clock_label = tk.Label(frame, textvariable=self.var_time,
                               **look.label_inv)
        clock_label.pack(side=tk.TOP, fill=tk.X, expand=True, **look.pack)

        btn_new = tk.Button(self, text="Nowa faktura",
                            command=self.new_invoice,
                            **look.button)
        btn_new.pack(fill=tk.X, **look.grid)

        self.clock_thread = ClockThread(self.update_clock)
        self.clock_thread.start()

    def update_clock(self, time):
        self.var_time.set(time)

    def new_invoice(self):
        self.master.show_page("SelectBuyerPage", "NewInvoicePage")

