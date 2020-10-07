import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Tkinter GUI')

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win,width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan = 3)


win.mainloop()