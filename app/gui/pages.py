import tkinter as tk
from app import controller
from app.gui import utils
from app.threads import ClockThread


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
        self.master.show_page("SelectBuyerPage", "NewInvoicePage")


class SelectBuyerPage(Page):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.buyers = {}
        self.next_page = None

        title_label = tk.Label(self, text="Wybierz nabywcę",
                               font=("TkDefaultFont", 16, "bold"), fg="#777")
        title_label.pack(side=tk.TOP, fill=tk.X)

        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.var_search = tk.StringVar()
        search_entry = tk.Entry(top_frame, textvariable=self.var_search)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        new_customer_btn = tk.Button(top_frame, text="Dodaj nowego",
                                     state=tk.DISABLED)
        new_customer_btn.pack()

        self.listbox, listbox_frame = utils.create_scrollable_listbox(self)
        listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.var_search.trace("w", lambda *_: self.on_search_changed())
        self.listbox.bind("<Double-1>", lambda _: self.on_buyer_selected())

        search_entry.focus_set()

    def on_shown(self, next_page):
        self.next_page = next_page
        self.update_buyer_list()

    def on_search_changed(self):
        self.update_buyer_list()

    def on_buyer_selected(self):
        if self.next_page is None:
            return

        selection = self.listbox.curselection()
        text = self.listbox.get(selection[0])
        buyer = self.buyers[text]

    def update_buyer_list(self):
        buyers = controller.search_buyers(self.var_search.get())
        self.buyers.clear()
        self.listbox.delete(0, tk.END)
        for buyer in buyers:
            text = buyer.to_str_row()
            if text not in self.buyers:
                self.buyers[text] = buyer
            self.listbox.insert(tk.END, text)

