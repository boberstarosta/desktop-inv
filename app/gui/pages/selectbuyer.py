import tkinter as tk
from app import controller
from app.gui import look, utils
from app.gui.pages import Page


class SelectBuyerPage(Page):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.buyers = {}
        self.next_page = None

        title_frame = tk.Frame(self, **look.frame_inv)
        title_frame.pack(side=tk.TOP, fill=tk.X)

        title_label = tk.Label(title_frame, text="Wybierz nabywcę",
                               **look.label_inv)
        title_label.pack(side=tk.TOP, fill=tk.X, **look.pack)

        top_frame = tk.Frame(self, **look.frame_inv)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.var_search = tk.StringVar()
        search_entry = tk.Entry(top_frame, textvariable=self.var_search,
                                **look.entry)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, **look.pack)

        new_customer_btn = tk.Button(top_frame, text="Nowy...",
                                     **look.button)
        new_customer_btn.pack(**look.pack)

        self.listbox, listbox_frame = \
            utils.create_scrollable_listbox(self, **look.listbox)
        listbox_frame.pack(fill=tk.BOTH, expand=True, **look.pack)

        self.var_search.trace("w", lambda *_: self.on_search_changed())
        self.listbox.bind("<Double-1>", lambda _: self.on_buyer_selected())
        self.listbox.bind("<Return>", lambda _: self.on_buyer_selected())
        self.listbox.bind("<KP_Enter>", lambda _: self.on_buyer_selected())

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
        self.master.show_page(self.next_page, buyer)

    def update_buyer_list(self):
        buyers = controller.search_buyers(self.var_search.get())
        self.buyers.clear()
        self.listbox.delete(0, tk.END)
        for buyer in buyers:
            text = buyer.to_str_row()
            if text not in self.buyers:
                self.buyers[text] = buyer
            self.listbox.insert(tk.END, text)

