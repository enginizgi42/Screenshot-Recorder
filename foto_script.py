from tkinter import *
import pyscreenshot
import datetime
from pathlib import Path
import os

root = Tk()
root.geometry("24x20")
root.attributes("-topmost", True)
root.geometry("+0+0")
root.overrideredirect(True)
root.resizable(False,False)




def photo():
    x=repr(datetime.datetime.now())
    PATH= os.path.join(Path.home(),"Desktop","{}.jpg".format(x))
    img = pyscreenshot.grab(childprocess=False)
    img.save(PATH)
def kapat(event):
    os._exit(0)
    


b1 = Button(root, text="SS", width=2, command = photo, bg = "RoyalBlue1")
b1.grid(row = 0, column = 0)
b1.bind("<Button-3>", kapat)



root.mainloop()
