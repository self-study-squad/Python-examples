# Python GUI Test 15

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


win = tk.Tk()
win.title("Python GUI")

#Create group Name input
ttk.Label(win,text = "Họ và tên: ").grid(column = 0,row = 0)

name = tk.StringVar()
nameEnt = ttk.Entry(win,width = 24,textvariable = name)
nameEnt.grid(column = 0, row = 1,padx=20)

# Create 3 checkbox
check1 = tk.IntVar()
ckbox1 = tk.Checkbutton(win,text="CheckBox1",state="disable",variable=check1)
ckbox1.grid(column = 0, row = 2)

check2 = tk.IntVar()
ckbox2 = tk.Checkbutton(win,text="Checkbox2",state="normal",variable=check2)
ckbox2.grid(column=1,row = 2)

check3 = tk.IntVar()
ckbox3 = tk.Checkbutton(win,text="Checkbox3",state="normal",variable=check3)
ckbox3.grid(column=2,row = 2)

#Create group Code input
ttk.Label(win,text = "Mã số: ").grid(column = 1, row = 0)

code = tk.StringVar()
codeEnt = ttk.Entry(win,width = 24, textvariable = code)
codeEnt.grid(column = 1, row = 1)


#Create Button
def SaveCommand():
    action.configure(text="Hello %s, your code is %s"%(name.get(),code.get()),state='disable')

action = ttk.Button(win,text="Save data",command = SaveCommand)
action.grid(column = 2, row = 1,padx = 20)

#ScrollText Widget
scr = scrolledtext.ScrolledText(win,width = 30, height=3,wrap = tk.WORD)
scr.grid(column = 0,columnspan = 3,row = 3)


#Radiobox
clRed="red"
clBlue="Blue"
clGreen="Green"

def RadCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background = clRed)
    if radSel == 2: win.configure(background = clBlue)
    if radSel == 3: win.configure(background = clGreen)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text=clRed, variable = radVar, value = 1,command = RadCall)
rad1.grid(column = 0, row = 4)

rad2 = tk.Radiobutton(win,text=clBlue, variable = radVar, value = 2, command = RadCall)
rad2.grid(column = 1, row = 4)

rad3 = tk.Radiobutton(win,text=clGreen, variable = radVar, value = 3, command = RadCall)
rad3.grid(column = 2, row = 4)

#Create a Menu
#Create a MenuBar
MenuBar = Menu(win)
win.config(menu=MenuBar)

#Add File menu onto the MenuBar
fileMenu = Menu(MenuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
# fileMenu.add_command(label="Exit")
MenuBar.add_cascade(label="File",menu=fileMenu)

#Add Help Menu
helpMenu = Menu(MenuBar,tearoff=0)
helpMenu.add_command(label="About")
MenuBar.add_cascade(label="Help",menu=helpMenu)

def _quit():
    win.quit()
    win.destroy()
    # exit()



fileMenu.add_command(label="Exit",command=_quit)


win.mainloop()