import tkinter as tk
import pathlib
from app.gui import look


def center_window(window):
    window.update()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(a) for a in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))


def set_window_icon(window, icon_file_name):
    icon_file = pathlib.Path.cwd() / pathlib.Path(icon_file_name)
    if icon_file.exists():
        try:
            img = tk.PhotoImage(file=icon_file)
            window.tk.call("wm", "iconphoto", window._w, img)
        except tk.TclError:
            print("Error loading icon file {}".format(icon_file))
    else:
        print("Icon file {} doesn't exist.".format(icon_file))


def create_scrollable_listbox(master, **listbox_kwargs):
    frame = tk.Frame(master, **look.frame)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    vscrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, **look.scrollbar)
    vscrollbar.grid(column=1, row=0, sticky=tk.NS)

    listbox = tk.Listbox(frame, **listbox_kwargs)
    listbox.grid(column=0, row=0, sticky=tk.NSEW, **look.grid)

    vscrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=vscrollbar.set)

    return listbox, frame
