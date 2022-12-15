from tkinter import *
from tkinter import ttk
class Frame():
    # Create Object
    root = Tk()
    
    # Set title
    root.title("Main Window")
    root.geometry("400x400")
    # Set Geometry
    root.__init__


    


    

    
    # Open New Window
    def launch(numWindows):
        global second
        second = Toplevel()
        second.title("Child Window")
        second.geometry("400x400")
    
    # Show the window
    def show():
        second.deiconify()
    
    # Hide the window
    def hide():
        second.withdraw()
    

    def __init__(self, numWindows):
        
        for i in range(numWindows):
            self.launch
    
    root.mainloop()

frame = Frame(6)
frame.__init__()


    