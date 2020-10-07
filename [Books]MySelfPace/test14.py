# Python IDE

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

lbframe = ttk.LabelFrame(win,text = 'Options')
lbframe.grid(column = 0, row = 1)
ttk.Label(lbframe,text="Example label").grid(column = 0, row = 1)
lbframe.grid(column = 0, row = 7, padx = 20, pady = 40)

win.mainloop()