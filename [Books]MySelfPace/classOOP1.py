#Module File for OOP

class OOP():
    def __init__(self):

        #Create Instance
        self.win=tk.Tk()

        #Add a title
        self.win.title("Python GUI")
        self.createwidgets()

        #Button callback
        def Clickme(self):
            self.action.configure(text="Hello "+self.name.get())

        def createWidgets(self):
            #Tab control introduce here
            tabControl = ttk.Notebook(self.win)
            tab1 = ttk.Frame(tabControl)
            tabControl.add(tab1,text="Tab1")
            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2,text="Tab2")

            tabControl.pack(expand=1,fill="both")




