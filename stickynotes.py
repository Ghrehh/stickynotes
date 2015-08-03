import os, wx, atexit

class StickyNotes():
    def __init__(self):
        self.save_exists = False
        self.list = [""]
        self.list_to_save = []

    def run(self):
        self.check_file()
        for line in self.list:
            frame = StickyFrame(None, 'Sticky Note', line)

    def check_file(self):
        if not os.path.exists("sn_save.txt"):
            f = file("sn_save.txt", "w+")
        if os.stat("sn_save.txt").st_size != 0:
            self.list = open("sn_save.txt").read().split("///%")


    def exit_save(self):
        to_save = "///%".join(self.list_to_save)
        file_ = open('sn_save.txt', 'w')
        file_.write(to_save)
        file_.close()


class StickyFrame(wx.Frame):
    def __init__(self, parent, title, words=""):
        wx.Frame.__init__(self, parent, title=title, size=(400,300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE, value=words)
        self.Show(True)

        filemenu= wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT,"&New Note","Opens a New Note")
        menuExit = filemenu.Append(wx.ID_EXIT,"Save and E&xit"," Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.Show(True)

    def OnExit(self,e):
        s.list_to_save.append(self.control.Value)
        self.Close(True)  # Close the frame.

    def OnAbout(self,e):
        frame = StickyFrame(None, 'Sticky Note')


app = wx.App(False)
s = StickyNotes()
s.run()
app.MainLoop()

atexit.register(s.exit_save)
