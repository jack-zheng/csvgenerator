from tkinter import *

root = Tk()

state_map = {}


def newChk(pos, r, c):
    state = IntVar()
    chk = Checkbutton(root, text=pos, variable=state)
    chk.grid(row=r, column=c)
    state_map[chk.cget('text')] = state

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
        newChk(sub, row, col)

        
def onClick():
    for sub in state_map:
        print('sub: %s, value: %s' %(sub, state_map[sub].get()))
btn = Button(root, text='try', command=onClick)
btn.grid(row=5, column=0)

root.mainloop()