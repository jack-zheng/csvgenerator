from tkinter import *
from tkinter.ttk import Frame, Button, Style
from tkinter import filedialog
import os
from generator import *


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.status_map = {}
        ret = [picks[i:i+6] for i in range(0, len(picks), 5)]
        for row, val in enumerate(ret):
            for col, pick in enumerate(val):
                var = IntVar()
                if pick in ['USERNAME', 'USERID']:
                    var.set(1)
                chk = Checkbutton(self, text=pick, variable=var)
                chk.grid(row=row, column=col)
                self.status_map[chk.cget('text')] = var


def main():
    root = Tk()
    root.geometry('500x700')
    root.title("User File Generator")

    file_path = StringVar()
    user_count = IntVar()
    status_map = {}

    style = Style()
    style.theme_use("default")

    def append_checkbox(picks):
        ret = [picks[i:i+6] for i in range(0, len(picks), 5)]
        for row, val in enumerate(ret):
            for col, pick in enumerate(val):
                var = IntVar()
                if pick in ['USERNAME', 'USERID']:
                    var.set(1)
                chk = Checkbutton(checkbox_frame, text=pick, variable=var)
                chk.grid(row=row, column=col)
                status_map[chk.cget('text')] = var

    def onClick():
        print('select file button clicked')
        abspath = filedialog.askopenfilename(initialdir=os.getcwd())
        print('---> select file name: %s' % abspath)

        header = get_file_header(abspath)
        append_checkbox(header)
        file_path.set(abspath)

    file_select_frame = Frame(root, relief=RAISED, borderwidth=1)
    file_select_frame.pack(fill=BOTH, expand=True)

    lbl = Label(file_select_frame, text="File Path")
    lbl.pack(side=LEFT)
    txt = Entry(file_select_frame, textvariable=file_path)
    txt.pack(side=LEFT)
    btn = Button(file_select_frame, text='Browse', command=onClick)
    btn.pack(side=LEFT)

    header_frame = Frame(root, relief=RAISED, borderwidth=1)
    header_frame.pack(fill=BOTH, expand=True)
    desclbl = Label(header_frame, text='All Header Supported')
    desclbl.pack(side=TOP)
    checkbox_frame = Frame(header_frame, relief=RAISED, borderwidth=1)
    checkbox_frame.pack(fill=BOTH, expand=True)


    user_count_frame = Frame(root, relief=RAISED, borderwidth=1)
    user_count_frame.pack(fill=BOTH, expand=True)
    spinlbl = Label(user_count_frame, text="How manay user you want?")
    spinlbl.pack(side=LEFT)
    spin = Spinbox(user_count_frame, from_=0, to=100, width=5, textvariable=user_count)
    spin.pack(side=LEFT)

    submit_frame = Frame(root, relief=RAISED, borderwidth=1)
    submit_frame.pack(fill=BOTH, expand=True)

    def process_submit():
        print('generate file start !')
        #print('file: %s, count: %s, increment column: %s' %(file_path, user_count, ))
        print('file: %s, count: %s' %(file_path.get(), user_count.get()))
        print('map: %s' % len(status_map))
        
        for sub in status_map:
            print('key: %s, value: %s' %(sub, status_map[sub].get()))


    submitBtn = Button(submit_frame, text="Submit", command=process_submit)
    submitBtn.pack(side=RIGHT)

    root.mainloop()

if __name__=='__main__':
    main()
