from tkinter import *
 
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
default_int = IntVar()
default_int.set(2)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=default_int)
spin.grid(column=0,row=0)
 
window.mainloop()
