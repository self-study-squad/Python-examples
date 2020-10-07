# GUI tkinter Entry

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# Modified Button Click function
def clickme():
    action.configure(text="Hello " + name.get(),state='disabled')



#Changing our label
ttk.Label(win,text='Enter a name:').grid(column=0,row=0)

# Adding a Textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=24, textvariable=name)
nameEntered.grid(column=0,row=1)
nameEntered.focus()

# Adding a Combo box
ttk.Label(win,text="Choose a code:").grid(column=1,row=0)
number = tk.StringVar()
numberChosen=ttk.Combobox(win,width=12,textvariable=number)
numberChosen['values']=(1,2,3,4,5,6)
numberChosen.grid(column=1,row=1)
numberChosen.current()

# Adding button outside
action = ttk.Button(win,text="Click to save input data",command=clickme)

# Position button in second row, second column
action.grid(column=1,row=2)


win.mainloop()