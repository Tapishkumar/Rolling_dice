import random
from tkinter import *

root = Tk()
root.geometry("700x450")
root.title("Rolling dice")

L1 = Label(root,text=' ', font=("Helvetica", 200))


def roll():

    number= ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    L1.config(text = f"{random.choice(number)}{random.choice(number)}")
    L1.pack()


B1 = Button(root, text="Lets roll...", command=roll)
B1.place(x=330, y=0)

root.mainloop()
