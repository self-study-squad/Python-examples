# Python GUI

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

#Label Username and Usercode
ttk.Label(win,text="Username: ").grid(column = 0,row = 0)
ttk.Label(win,text="UserDefCode: ").grid(column = 0,row = 1)
ttk.Label(win,text="UserOrdCode: ").grid(column = 0,row = 2)

#Build entry for Username
uname = tk.StringVar()
UNbox = ttk.Entry(win,width=24,textvariable = uname)
UNbox.grid(column = 1, row = 0)
UNbox.focus()

#Build entry for UserDefCode
udcode = tk.StringVar()
UDbox = ttk.Combobox(win,width = 24, textvariable = udcode,state='readonly')
UDbox['values'] = ('G00','G01','G02','G03','G04','G05','G06','G07','G08','G09','G10','G11','G12')
UDbox.grid(column = 1, row = 1)
UDbox.current('00')

#Build entry for UserOrdCode
uocode = tk.StringVar()
UObox = ttk.Combobox(win,width = 24, textvariable = uocode,state = 'readonly')
UObox['values'] = ('N00','N01','N02','N03','N04','N05','N06','N07','N08','N09','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20')
UObox.grid(column = 1, row = 2)
UObox.current('00')

#Create button function
def SaveStuData():
    submit.configure(text="Hello " + uname.get() + ", your code is: " + udcode.get() + uocode.get(),state = 'disabled')
    
submit = ttk.Button(win,text="Submit info",command = SaveStuData)
submit.grid(column = 1,row = 4)

#Create 3 check button
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text="Disable",state = 'disable',variable = chVarDis)
check1.select()
check1.grid(column = 0, row = 5,sticky = tk.W)

chVarEn1 = tk.IntVar()
check2 = tk.Checkbutton(win, text="Enable", variable = chVarEn1)
check2.deselect()
check2.grid(column = 1, row = 5, sticky = tk.W)

chVarEn2 = tk.IntVar()
check3 = tk.Checkbutton(win,text = "Enable wc",variable = chVarEn2)
check3.select()
check3.grid(column = 2, row = 5, sticky = tk.W)

win.mainloop()