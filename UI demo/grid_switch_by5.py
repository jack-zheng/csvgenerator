from tkinter import *

root = Tk()

def newBtn(pos, r, c):
    btn = Button(root, text=pos)
    btn.grid(row=r, column=c)

def chunks(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]

a = ['The',
 'first',
 'geometry',
 'manager',
 'of',
 'Tk',
 'had',
 'been',
 'pack.',
 'The',
 'algorithmic',
 'behaviour',
 'of',
 'pack',
 'is',
 'not',
 'easy',
 'to']

ret = chunks(a, 5)
for row, val in enumerate(ret):
    for col, sub in enumerate(val):
        newBtn(sub, row, col)


root.mainloop()