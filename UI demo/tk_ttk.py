from tkinter import *
from tkinter.ttk import *
 
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)
 
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=1)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)

window.mainloop()
