import tkinter as tk
from app.gui import look
from app.models import Item


class ItemRow:
    def __init__(self, master, index, item=None):
        self.master = master
        self.index = index
        if item is None:
            item = Item()
        self.item = item

        self.var_name = tk.StringVar()
        name_entry = tk.Entry(master, textvariable=self.var_name,
                              **look.entry)
        name_entry.grid(column=0, row=index + 1, sticky=tk.EW, **look.grid)

        self.var_unit = tk.StringVar()
        unit_entry = tk.Entry(master, textvariable=self.var_unit,
                              **look.entry)
        unit_entry.grid(column=1, row=index + 1, sticky=tk.EW, **look.grid)


class ItemList(tk.Frame):
    def __init__(self, master, items=[], **kwargs):
        super().__init__(master, **kwargs)

        self.itemrows = []

        captions = [
            "Nazwa", "j.m.", "Ilość", "Cena\njednostkowa\nnetto",
            "Wartość\nnetto", "Stawka\nVAT", "Wartość\nVAT", "Wartość\nbrutto"]

        for column, caption in enumerate(captions):
            label = tk.Label(self, text=caption, **look.label_inv)
            self.grid_columnconfigure(column, weight=1)
            label.grid(column=column, row=0, sticky=tk.EW)

        self.update_itemrows(items)

        self.add_button = tk.Button(self, text="Dodaj", command=self.add,
                                    **look.button)
        self.add_button.grid(column=0, row=len(self.itemrows) + 2,
                             sticky=tk.EW, **look.grid)

        if not self.itemrows:
            self.add()

    def update_itemrows(self, items):
        self.itemrows = [ItemRow(self, i, item)
                         for i, item in enumerate(items)]
        for itemrow in self.itemrows:
            pass

    def add(self):
        itemrow = ItemRow(self, len(self.itemrows))
        self.itemrows.append(itemrow)
        self.add_button.grid(row=len(self.itemrows) + 2)
