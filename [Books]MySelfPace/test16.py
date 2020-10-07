# Python GUI - Tab item

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import *

from tkinter import Menu

import class_ToolTip as ToolTip


#Create a Class for ToolTips
class ToolTip(object):
    def __init__(self,widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self,text):
        "Display text in Tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x,y,_cx,cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() +27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d"%(x,y))

        label = tk.Label(tw,text = self.text,justify = tk.LEFT,background="#ffffe0",relief=tk.SOLID,borderwidth=1,font=("tahoma","8","normal"))
        label.pack(ipadx = 1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
#==============================================================================================================


#Create ToolTip def
def createToolTip(widget,text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>',enter)
    widget.bind('<Leave>',leave)

    
#Create GUI
win = tk.Tk()
win.title("Python GUI")

win.iconbitmap(r'PyIcon\iconfinder_application-x-python_8974.ico')

#Create Frame
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text="Tab1")
createToolTip(tab1,"Tab 1 of frame")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text="Tab2")
createToolTip(tab2,"Tab 2 of frame")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3,text="Tab3")
createToolTip(tab3,"Tab 3 of frame")

tabControl.pack(expand=1,fill="both")

monty1 = ttk.LabelFrame(tab1,text = "Monty Python")
monty1.grid(column = 0, row = 0, padx = 8, pady = 4)
ttk.Label(monty1,text="Enter a name: ").grid(column=0, row=0,sticky="W")

#Create Entry in Frame
name = tk.StringVar()
nameEnt = ttk.Entry(monty1,width=24, textvariable=name)
nameEnt.grid(column=0,row=1)
createToolTip(nameEnt,"Please enter a name here!")

#Create ComboBox in Frame
ttk.Label(monty1,text="Choose a number: ").grid(column=1,row=0)

num = tk.StringVar()
numCh = ttk.Combobox(monty1,width=14,textvariable=num)
numCh['values']=(1,2,3,4,5)
numCh.grid(column=1,row=1,padx=8, pady=4)
numCh.current(1)
createToolTip(numCh,"Please choose a number!")
#Create Button in Frame
def ClickMe():
    action.configure(text="Hello "+name.get(),state="disabled")

action = ttk.Button(monty1,text="Save Data",command = ClickMe)
action.grid(column=2,row=1)

#Adding a Spinbox Command
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT,value+'\n')

def _spin1():
    value = spin1.get()
    print(value)
    scr.insert(tk.INSERT,value+"\n")

#Adding a Spinbox Widget
spin = Spinbox(monty1,from_=0, to=10,width=5,bd=7,command=_spin)
spin.grid(column=0,row=2,sticky="W")

#Adding 2nd Spinbox
spin1 = Spinbox(monty1,values=(0,50,100),from_=0,to=10,width=5,bd=7,command=_spin1,relief=tk.RIDGE)
spin1.grid(column=1,row=2)


#Python ScrolledText
scrolW = 40
scrolH = 10
scr = scrolledtext.ScrolledText(monty1,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)
createToolTip(scr,"This is a scrolltext widget.")


#Create Tab2
monty2 = ttk.LabelFrame(tab2,text="The Snake")
monty2.grid(column=0,row=0,padx=8,pady=4)

#Check Button
CheckVar1 = tk.IntVar()
CheckBut1 = tk.Checkbutton(monty2,text="Disable",state="disabled",variable=CheckVar1)
CheckBut1.select()
CheckBut1.grid(column = 0, row = 2)

CheckVar2 = tk.IntVar()
CheckBut2 = tk.Checkbutton(monty2,text="Unchecked",state="active",variable=CheckVar2)
CheckBut2.grid(column = 1, row = 2)

CheckVar3 = tk.IntVar()
CheckBut3 = tk.Checkbutton(monty2,text="Checked",state="active",variable=CheckVar3)
CheckBut3.select()
CheckBut3.grid(column=2, row = 2)

#Create RadioButtons
clred="Red"
clblue="Blue"
clgreen="Green"


def RadCall():
    RadSel = RadVal.get()
    if RadSel == 1: monty2.configure(text=clred)
    if RadSel == 2: monty2.configure(text=clblue)
    if RadSel == 3: monty2.configure(text=clgreen)

RadVal = tk.IntVar()

Opt1 = tk.Radiobutton(monty2,text="Red",variable=RadVal,value=1,command=RadCall)
Opt1.grid(column=0,row=4)

Opt2 = tk.Radiobutton(monty2,text="Blue",variable=RadVal,value=2,command=RadCall)
Opt2.grid(column=1,row=4)

Opt3 = tk.Radiobutton(monty2,text="Green",variable=RadVal,value=3,command=RadCall)
Opt3.grid(column=2, row=4)

#Create the MenuBar
menuBar = Menu(win)
win.config(menu=menuBar)

#Create File Menu
fileMenu = Menu(menuBar)
fileMenu.add_command(label="New")
menuBar.add_cascade(label="File",menu=fileMenu)


#Display a message box
#Callback function
def _msgBox():
    # mBox.showinfo("Python Message Info Box","A Python GUI created using tkinter: \n The year 2015.")
    answer = mBox.askyesno("Python Yes/No CheckBox","Do you want to apply for this task?")
    print(answer)

#Create Help Menu
helpMenu = Menu(menuBar)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help",menu=helpMenu)

strData = spin1.get()
print("Spinbox Value: "+ strData)

#Place cursor into the entry
nameEnt.focus()

win.mainloop()