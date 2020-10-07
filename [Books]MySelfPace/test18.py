# Import Thread working job
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox

import B04829_Ch06_ToolTip as tt

from threading import Thread
import classOOP as cop

#Start GUI
oop = cop.OOP()



#Running method in thread

runT = Thread(target = oop.methodInAThread)
oop.win.mainloop()