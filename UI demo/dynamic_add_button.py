from tkinter import *

def onClick():
    print('Add...')
    tbtn = Button(frame, text='tmp')
    tbtn.pack()

root = Tk()
btn = Button(root, text='Add', command=onClick)
frame = Frame(root, width=200, height=100)

btn.pack(side=TOP)
frame.pack(side=BOTTOM)

root.mainloop()