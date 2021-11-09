from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import fitz


class Application(Tk):
    def __init__(self):
        super(Application, self).__init__()
        self.title("Pdf2jpg")
        self.minsize(640, 400)
        # self.wm_iconbitmap('icon.ico')
        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.browse()

    def browse(self):
        self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=1, row=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("Pdf files", "*.pdf"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        self.convert()

    def convert(self):
        self.cbutton = ttk.Button(self.labelFrame, text="Convert", command=self.pdf2jpg)
        self.cbutton.grid(column=1, row=3)

    def pdf2jpg(self):
        self.pdffile = self.filename
        self.doc = fitz.open(self.pdffile)
        self.page = self.doc.loadPage(0)
        self.pix = self.page.getPixmap()
        self.pix.writePNG("convert1.png")


app = Application()

app.mainloop()
