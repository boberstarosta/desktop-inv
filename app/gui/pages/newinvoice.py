import tkinter as tk
import datetime
from app import controller
from app.models import Invoice
from app.gui import look
from app.gui.itemlist import ItemList
from app.gui.pages import Page
from app.gui.scroll import VerticalScrollFrame


class NewInvoicePage(Page):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.invoice = None

        heading_frame = tk.Frame(self, **look.frame_inv)
        heading_frame.pack(side=tk.TOP, fill=tk.X)

        heading_label = tk.Label(heading_frame, text="Faktura VAT",
                                 **look.label_inv)
        heading_label.pack(side=tk.LEFT, fill=tk.X, expand=True, **look.pack)

        self.var_number = tk.StringVar()
        number_label = tk.Label(heading_frame, textvariable=self.var_number,
                                **look.label_inv)
        number_label.pack(side=tk.LEFT, fill=tk.X, expand=True, **look.pack)

        date_frame = tk.Frame(self, **look.frame)
        date_frame.pack(side=tk.TOP, fill=tk.X)

        date_caption_label = tk.Label(date_frame,
                                      text="Data wystawienia faktury",
                                      **look.label)
        date_caption_label.pack(side=tk.LEFT, fill=tk.X, expand=True,
                                **look.pack)

        self.var_date = tk.StringVar()
        date_label = tk.Label(date_frame, textvariable=self.var_date,
                              **look.label)
        date_label.pack(side=tk.LEFT, fill=tk.X, expand=True, **look.pack)

        date_button = tk.Button(date_frame, text="Zmień...",
                                command=self.on_change_date_clicked,
                                **look.button)
        date_button.pack(side=tk.LEFT, fill=tk.X, **look.pack)

        buyer_frame = tk.Frame(self, **look.frame)
        buyer_frame.pack(side=tk.TOP, fill=tk.X)

        buyer_caption_label = tk.Label(buyer_frame, text="Nabywca",
                                       **look.label)
        buyer_caption_label.pack(side=tk.LEFT, fill=tk.X, expand=True,
                                 **look.pack)

        self.var_buyer_data = tk.StringVar()
        buyer_data_label = tk.Label(buyer_frame,
                                    textvariable=self.var_buyer_data,
                                    justify=tk.LEFT,
                                    **look.label)
        buyer_data_label.pack(side=tk.LEFT, fill=tk.X, expand=True,
                              **look.pack)

        buyer_button = tk.Button(buyer_frame, text="Zmień...",
                                 command=self.on_change_buyer_clicked,
                                 **look.button)
        buyer_button.pack(side=tk.LEFT, fill=tk.X, **look.pack)

        markup_frame = tk.Frame(self, **look.frame)
        markup_frame.pack(side=tk.TOP, fill=tk.X)

        self.var_markup = tk.IntVar()
        self.markup_checkbox = tk.Checkbutton(markup_frame,
                                              text="Procedura marży",
                                              variable=self.var_markup,
                                              **look.checkbutton)
        self.markup_checkbox.pack(fill=tk.X, **look.pack)

        scroll_frame = VerticalScrollFrame(self, **look.frame)
        scroll_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,
                          **look.pack)

        self.item_list = ItemList(scroll_frame.interior, height=900, **look.frame_inv)
        self.item_list.pack(side=tk.TOP, 
                            **look.pack)

    def on_shown(self, buyer=None):
        if self.invoice is None:
            self.invoice = Invoice(
                date=datetime.date.today(),
                number=controller.generate_invoice_number())
        if buyer is not None:
            self.invoice.buyer = buyer
        self.update_number_label()
        self.update_date_label()
        self.update_buyer_data_label()

    def on_change_date_clicked(self):
        pass

    def on_change_buyer_clicked(self):
        self.master.push_page("SelectBuyerPage")

    def update_number_label(self):
        self.var_number.set("Numer " + self.invoice.get_number_str())

    def update_date_label(self):
        self.var_date.set("{}".format(self.invoice.date))

    def update_buyer_data_label(self):
        self.var_buyer_data.set(self.invoice.buyer.to_text())
