# Test on new independent standalone message box

from tkinter import Tk  
from tkinter import messagebox as mBox

root = Tk()
root.withdraw()

mBox.showinfo('Python GUI MessageBox',"A GUI created in 2019")

#Change the main windows Icon
root.iconbitmap(r'C:\Python34\DLLs\pyc.ico')
