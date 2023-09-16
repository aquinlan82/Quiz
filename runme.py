from tkinter import *
from helpers import *


 
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Python Tkinter")
        self.minsize(500,400)
 

read_text_quiz("capitals", "capitals.txt")
root = Root()
root.mainloop()