# Continue on GUI

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# Modify and adding label
aLabel = ttk.Label(win,text="A label")
aLabel.grid(column=0,row=0)

# Button click event callback funciton
def clickme():
    action.configure(text="** Text Changed to red!! **")
    aLabel.configure(background='yellow',foreground='red')

# Adding a button
action = ttk.Button(win,text='Click me to change text!!', command=clickme)
action.grid(column=1,row=0)

win.mainloop()
