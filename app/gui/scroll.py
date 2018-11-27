import tkinter as tk
import platform


OS = platform.system()


class VerticalScrollFrame(tk.Frame):
    active_widget = None

    def __init__(self, parent):
        super().__init__(parent)

        vscrollbar = tk.Scrollbar(self, orient="vertical")
        vscrollbar.pack(fill="y", side="right", expand=False)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                yscrollcommand=vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        vscrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.interior = interior = tk.Frame(self.canvas)
        interior_id = self.canvas.create_window(0, 0, window=interior,
                                                anchor="nw")

        def _configure_interior(event):
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(interior_id,
                                          width=self.canvas.winfo_width())

        self.canvas.bind('<Configure>', _configure_canvas)

        self.interior.bind("<Enter>", lambda e: self._set_active())
        self.interior.bind("<Leave>", lambda e: self._set_inactive())

        on_mousewheel = self._get_mousewheel_handler()

        if OS == "Linux" :
            self.bind_all('<4>', on_mousewheel)
            self.bind_all('<5>', on_mousewheel)
        else:
            self.bind_all("<MouseWheel>", on_mousewheel)

    @staticmethod
    def _get_mousewheel_handler():
        if OS == "Linux":
            def on_mousewheel(event):
                if VerticalScrollFrame.active_widget is not None:
                    if event.num == 4:
                        VerticalScrollFrame.active_widget.canvas.yview_scroll(
                            -1, "units")
                    elif event.num == 5:
                        VerticalScrollFrame.active_widget.canvas.yview_scroll(
                            1, "units")
        elif OS == "Windows":
            def on_mousewheel(event):
                if VerticalScrollFrame.active_widget is not None:
                    VerticalScrollFrame.active_widget.canvas.yview_scroll(
                        -1*(event.delta//120), "units")

        return on_mousewheel

    def _set_active(self):
        VerticalScrollFrame.active_widget = self

    def _set_inactive(self):
        VerticalScrollFrame.active_widget = None
