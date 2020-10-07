# Test 12 on GUI Database

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python IDE")

# Label Username for Entry
ttk.Label(win,text='Username').grid(column = 0, row = 0)

# Entry input
uname = tk.StringVar()
unEntry = ttk.Entry(win,width = 24,textvariable = uname)
unEntry.grid(column = 0, row = 1)
unEntry.focus()

# Label for Combobox
ttk.Label(win,text='Choices').grid(column = 0, row = 2)
# Conbobox input
ucode = tk.IntVar()
unCombo = ttk.Combobox(win,width = 24,textvariable = ucode)
unCombo['values']=(1,3,5)
unCombo.grid(column = 0, row = 3)

# Input Button
def butt():
    SaveData.configure(text="Data saved! Your name is " + uname.get() + ", code: " + str(ucode.get()),state ='disable')


# Create Button
SaveData = ttk.Button(win,text="Save Data",command = butt)
SaveData.grid(column = 1, row = 3)

# Create RadioButtons
# Radiobuttons Global Value
COLOR1 = 'Red'
COLOR2 = 'alice blue'
COLOR3 = 'Green'

# Radiobuttons Callback
def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background = COLOR1)
    if radSel == 2: win.configure(background = COLOR2)
    if radSel == 3: win.configure(background = COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text = COLOR1, variable = radVar, value = 1, command = radCall)
rad1.grid(column = 0, row = 4, sticky = tk.W)

rad2 = tk.Radiobutton(win,text = COLOR2, variable = radVar, value = 2, command = radCall)
rad2.grid(column = 1, row = 4, sticky = tk.W)

rad3 = tk.Radiobutton(win,text = COLOR3, variable = radVar, value = 3, command = radCall)
rad3.grid(column = 3, row = 4, sticky = tk.W)

win.mainloop()