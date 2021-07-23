import fitz
from tkinter import *
from tkinter import filedialog,ttk

class Application(Tk):
    def __init__(self):

        super(Application,self).__init__()
        self.title("Pdftojpg")

app=Application()
app.mainloop()