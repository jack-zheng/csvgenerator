from tkinter import *


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   root = Tk()
   def generate_checkbox():
      val = entry.get().split(',')
      print('type: %s' % type(val))
      print('val: %s' % val)
      Checkbar(root, val).pack(side=BOTTOM)
      print('picked')

   entry = Entry(root)
   btn = Button(root, text='add', command=generate_checkbox)

   entry.pack(side=LEFT)
   btn.pack(side=LEFT)


   #lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   ##tgl = Checkbar(root, ['English','German'])
   #ng.pack(side=TOP,  fill=X)
   #tgl.pack(side=LEFT)
   #lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()