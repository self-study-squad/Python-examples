import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from time import sleep
import B04829_Ch06_ToolTip as tt

class OOP():

        def methodInAThread(self):
            print("Hi there, how are you?")
            
        def createThread(self):
            runT = Thread(target=self.methodInAThread)
            runT.start()

        #Button callback
        def Clickme(self):
            self.action.configure(text="Hello "+self.name.get())
            self.createThread()

        #Adding non-threading code with sleep freezed the GUI
            for idx in range(10):
                sleep(5)
                self.scr.insert(tk.INSERT, str(idx) + '\n') 

        def createWidgets(self):
            #Tab control introduce here
            tabControl = ttk.Notebook(self.win)
            
            tab1 = ttk.Frame(tabControl)
            tabControl.add(tab1,text="Tab1")
            tt.createToolTip(tab1,"First Tab of Frame")

            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2,text="Tab2")
            tt.createToolTip(tab2,"Second Tab of Frame")

            tabControl.pack(expand=1,fill="both")  


        def __init__(self):
            #Create Instance
            self.win = tk.Tk()

            #Add a title
            self.win.title("Python GUI")
            self.createWidgets()
            self.win.iconbitmap(r'PyIcon\iconfinder_application-x-python_8974.ico')


