# https://www.python-course.eu/tkinter_dialogs.php
from tkinter import filedialog
filename = filedialog.askopenfilename()
print('--> ret: %s' % filename)
#filename = filedialog.asksaveasfilename()
#dirname = filedialog.askdirectory()
