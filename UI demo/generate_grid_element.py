from tkinter import *

root = Tk()

def newBtn(pos):
    btn = Button(root, text=pos)
    btn.grid(row=i, column=j)

i = 10
while i>0:
    # generate grid row
    j = 10
    while j > 0:
        btn = Button(root, text=str(i)+','+str(j))
        btn.grid(row=i, column=j)
        j = j - 1
    # index --
    i = i - 1

root.mainloop()