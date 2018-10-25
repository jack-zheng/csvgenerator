# set_size.py, customize the default frame size when app start

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(700, 700))


def main():

    app = wx.App()
    ex = Example(None, title='Sizing')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()