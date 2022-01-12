# hello_wx_class.py
# basic GUI but with a class

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super()._init_(None, title = 'Hello World')
        self.Show()

if __name__== '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()