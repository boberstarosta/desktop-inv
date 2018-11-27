import tkinter as tk


class DataEntry(tk.Frame):
    """Entry chenging value only after enter key and input validation

        Usage:
        Use the 'value' attribute to access the value,
        pack/place/grid normally.
    """

    def __init__(self, parent, value="", trace_func=None):
        super().__init__(parent)

        self.trace_func = trace_func

        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack(fill=tk.BOTH, expand=True)

        self._value = value
        self.entry.insert(0, self.convert_to_str(self._value))

        self.defaultcolor = self.entry.cget("bg")
        self.validcolor = "#AAFFCC"
        self.invalidcolor = "#FF9999"

        self.var.trace("w", self.on_changed)
        self.entry.bind("<Return>", self.confirm)
        self.entry.bind("<KP_Enter>", self.confirm)
        self.entry.bind("<Escape>", self.cancel)
        self.entry.bind("<FocusOut>", self.cancel)

    @property
    def value(self):
        return self._value

    def on_changed(self, *args):
        if self.validate():
            if self.convert_from_str(self.var.get()) == self._value:
                self.entry.configure(bg=self.defaultcolor)
            else:
                self.entry.configure(bg=self.validcolor)
        else:
            self.entry.configure(bg=self.invalidcolor)

    def confirm(self, event):
        if self.validate():
            newvalue = self.convert_from_str(self.var.get())
            if self._value != newvalue:
                self._value = newvalue
                self.var.set(self.convert_to_str(self._value))
                if self.trace_func is not None:
                    self.trace_func(self)
            self.master.focus()
        else:
            self.cancel(event)

    def cancel(self, event):
        self.var.set(self.convert_to_str(self._value))
        self.entry.configure(bg=self.defaultcolor)
        self.master.focus()

    def validate(self):
        """"Return True if self.var.get() value is a valid input"""
        return True

    def convert_from_str(self, s):
        return s

    def convert_to_str(self, v):
        return str(v)
