from tkinter import *
from tkinter import filedialog
from generator import *
import os


def main():
    root = Tk()
    root.title("User File Generator")

    file_path = StringVar()
    user_count = IntVar()
    status_map = {}

    def append_checkbox(picks):
        ret = [picks[i:i+3] for i in range(0, len(picks), 3)]
        for row, val in enumerate(ret):
            for col, pick in enumerate(val):
                var = IntVar()
                if pick in ['USERNAME', 'USERID']:
                    var.set(1)
                chk = Checkbutton(checkbox_frame, text=pick, variable=var)
                chk.grid(row=row, column=col, sticky=W, padx=5)
                status_map[chk.cget('text')] = var

    def onClick():
        print('select file button clicked')
        abspath = filedialog.askopenfilename(initialdir=os.getcwd())
        print('---> select file name: %s' % abspath)

        header = get_file_header(abspath)
        append_checkbox(header)
        file_path.set(abspath)

    file_select_frame = Frame(root, relief=RAISED, borderwidth=1)
    file_select_frame.pack(fill=BOTH)

    lbl = Label(file_select_frame, text="File Path")
    lbl.pack(side=LEFT)
    txt = Entry(file_select_frame, textvariable=file_path)
    txt.pack(side=LEFT, expand=1, fill='both')
    btn = Button(file_select_frame, text='Browse', command=onClick)
    btn.pack(side=RIGHT)

    header_frame = Frame(root, relief=RAISED, borderwidth=1)
    header_frame.pack(fill=BOTH)
    desclbl = Label(header_frame, text='All Header Supported')
    desclbl.pack(side=TOP)
    checkbox_frame = Frame(header_frame, width=300, height=400, relief=RAISED, borderwidth=1)
    checkbox_frame.pack(fill=BOTH)


    user_count_frame = Frame(root, relief=RAISED, borderwidth=1)
    user_count_frame.pack(fill=BOTH)
    spinlbl = Label(user_count_frame, text="How manay user you want?")
    spinlbl.pack(side=LEFT)
    spin = Spinbox(user_count_frame, from_=0, to=100, width=5, textvariable=user_count)
    spin.pack(side=LEFT)

    submit_frame = Frame(root, relief=RAISED, borderwidth=1)
    submit_frame.pack(fill=BOTH)

    def process_submit():
        print('generate file start !')
        #print('file: %s, count: %s, increment column: %s' %(file_path, user_count, ))
        print('file: %s, count: %s' %(file_path.get(), user_count.get()))
        print('map: %s' % len(status_map))

        target_col = []
        for sub in status_map:
            print('key: %s, value: %s' %(sub, status_map[sub].get()))
            if status_map[sub].get() == 1:
                target_col.append(sub)

        generate_general_csv(file_path.get(), user_count.get(), target_col)


    submitBtn = Button(submit_frame, text="Submit", command=process_submit)
    submitBtn.pack(side=RIGHT)

    root.mainloop()

if __name__=='__main__':
    main()
