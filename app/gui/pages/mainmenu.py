import tkinter as tk
from app.threads import ClockThread
from app.gui.pages import Page


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
        btn_new.pack(fill=tk.X, expand=True)

    def update_clock(self, time):
        self.var_time.set(time)

    def new_invoice(self):
        self.master.show_page("SelectBuyerPage", "NewInvoicePage")

