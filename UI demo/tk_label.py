from tkinter import *
 
window = Tk()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello", font=('Arial Bold', 10))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=1)
def clicked():
    lbl.configure(text='Button was clicked')

def fetch_input():
    res = 'fetch content: ' + txt.get()
    lbl.configure(text=res)

btn = Button(window, text='Click', command=clicked, bg='orange', fg='red')
btn.grid(column=1, row=0) 
btn2 = Button(window, text='Fetch Input', command=fetch_input, bg='orange', fg='red')
btn2.grid(column=1, row=1) 

txt2 = Entry(window, width=10, state='disabled')
txt2.grid(column=0, row=3)

window.mainloop()
