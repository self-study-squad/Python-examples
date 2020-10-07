# Test 08 - Python Tkinker
import tkinter as tk
from tkinter import ttk

win = tk.Tk();
win.title('Python Program')
ttk.Label(win,text="A label").grid(column=0,row=0)

win.mainloop()