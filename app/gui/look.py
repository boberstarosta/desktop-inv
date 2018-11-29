import tkinter as tk


WHITE = "#fff"
BLUE = "#4286f4"
GREEN = "#4ca522"
RED = "#e22222"
DARKGREEN = "#255111"

PADDING = 10

FONT = ("TkDefaultFont", 14, "bold")
FONT_MONO = ("TkFixedFont", 14, "bold")
FONT_LARGE = ("TkDefaultFont", 20, "bold")
FONT_LARGE_MONO = ("TkFixedFont", 20, "bold")


pack = {
    'padx': PADDING,
    'pady': PADDING,
}    

grid = {
    'padx': PADDING,
    'pady': PADDING,
}    


frame = {
    'background': WHITE,
}

frame_inv = {
    'background': BLUE,
}

label = {
    'font': FONT,
    'background': WHITE,
    'foreground': BLUE,
}

label_inv = {
    'font': FONT,
    'background': BLUE,
    'foreground': WHITE,
}

button = {
    'font': FONT,
    'relief': tk.FLAT,
    'padx': PADDING,
    'pady': PADDING,
    'borderwidth': 0,
    'background': GREEN,
    'foreground': WHITE,
    'activebackground': WHITE,
    'activeforeground': GREEN,
    'highlightbackground': GREEN,
    'disabledforeground': DARKGREEN,
}

entry = {
    'font': FONT,
    'borderwidth': PADDING,
    'relief': tk.FLAT,
    'background': WHITE,
    'foreground': BLUE,
    'highlightthickness': 0,
    'insertbackground': BLUE,
    'selectbackground': BLUE,
    'selectforeground': WHITE,
}

listbox = {
    'font': FONT,
    'relief': tk.FLAT,
    'background': WHITE,
    'foreground': BLUE,
    'activestyle': tk.NONE,
    'selectbackground': GREEN,
    'selectforeground': WHITE,
    'selectborderwidth': 0,
    'highlightthickness': 0
}

scrollbar = {
    'relief': tk.FLAT,
    'activerelief': tk.FLAT,
    'background': BLUE,
    'troughcolor': WHITE,
    'borderwidth': 0,
    'elementborderwidth': 0,
}

