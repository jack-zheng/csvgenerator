from tkinter import *

root = Tk()

val = StringVar()

entry = Entry(root, textvariable=val)
val.set('def')
entry.pack()

def onClick():
    tmp = entry.get() + '-append'
    print(tmp)
    val.set(tmp)

btn = Button(root, text='Change', command=onClick)
btn.pack()

root.mainloop()