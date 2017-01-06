## boook gui ##
# (c) brunston 2016 #
# GNU GPL #

from tkinter import *
from boook import *

class App:
    
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        self.display_scrollbar = Scrollbar(frame)
        self.display = Text(frame, height=20, width=80)
        self.display_scrollbar.grid(column=1, sticky=N+S)
        self.display.grid(row=0, column=0)
        self.quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit.grid(row=1, column=0)
        self.list = Button(frame, text="list", command=self.list)
        self.list.grid(row=1, column=1)
        
        self.library = DB("mylib")
        self.library.read()
    
        

    def list(self):
        for book in self.library.db["books"]:
            self.display.insert(END, book_title[book])
root = Tk()
app = App(root)

root.mainloop()
root.destroy()
             
