import tkinter as tk
import pathlib


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
