import wx


class mainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(mainFrame, self).__init__(*args, **kwargs)

        self.GUI()
        self.SetSize((618,575))

    def GUI(self):


        panelOne = wx.Panel(self, pos=((0,0)), size=((618,50)))
        panelOne.SetBackgroundColour("White")
        panelTwo = wx.Panel(self, pos=((0,52)), size=((618,50)))
        panelTwo.SetBackgroundColour("White")
        panelThree = wx.Panel(self, pos=((0,104)), size=((618,50)))
        panelThree.SetBackgroundColour("White")
        panelFour = wx.Panel(self, pos=((0,156)), size=((618,50)))
        panelFour.SetBackgroundColour("White")
        panelFive = wx.Panel(self, pos=((0,208)), size=((618,50)))
        panelFive.SetBackgroundColour("White")
        panelSix = wx.Panel(self, pos=((0,260)), size=((618,50)))
        panelSix.SetBackgroundColour("White")
        panelSeven = wx.Panel(self, pos=((0,312)), size=((618,50)))
        panelSeven.SetBackgroundColour("White")
        panelEight = wx.Panel(self, pos=((0,364)), size=((618,50)))
        panelEight.SetBackgroundColour("White")
        panelNine = wx.Panel(self, pos=((0,416)), size=((618,50)))
        panelNine.SetBackgroundColour("White")
        panelTen = wx.Panel(self, pos=((0,468)), size=((618,50)))
        panelTen.SetBackgroundColour("White")

#        mondayOne = wx.StaticText(panelTwo, -1, "ECE-450\nECE A123", pos=(110,60))
#        mondayOne.SetForegroundColour("Black")

        greyPanel = wx.Panel(self, pos=(0,0), size=(100,575))
        greyPanel.SetBackgroundColour("Grey")


        vertPanel = wx.Panel(self, pos=(100,0), size=((2,550)))
        vertPanel.SetBackgroundColour("Black")
        vertPanelTwo = wx.Panel(self, pos=(200,0), size=((2,550)))
        vertPanelTwo.SetBackgroundColour("Black")
        vertPanelThree = wx.Panel(self, pos=(300,0), size=((2,550)))
        vertPanelThree.SetBackgroundColour("Black")
        vertPanelFour = wx.Panel(self, pos=(400,0), size=((2,550)))
        vertPanelFour.SetBackgroundColour("Black")
        vertPanelFive = wx.Panel(self, pos=(500,0), size=((2,550)))
        vertPanelFive.SetBackgroundColour("Black")
        vertPanelSix = wx.Panel(self, pos=(600,0), size=((2,550)))
        vertPanelSix.SetBackgroundColour("Black")

        horPanel = wx.Panel(self, pos=(0,50), size=(720,2))
        horPanel.SetBackgroundColour("Black")
        horPanelTwo = wx.Panel(self, pos=(0,102), size=(720,2))
        horPanelTwo.SetBackgroundColour("Black")
        horPanelThree = wx.Panel(self, pos=(0,154), size=(720,2))
        horPanelThree.SetBackgroundColour("Black")
        horPanelFour = wx.Panel(self, pos=(0,206), size=(720,2))
        horPanelFour.SetBackgroundColour("Black")
        horPanelFive = wx.Panel(self, pos=(0,258), size=(720,2))
        horPanelFive.SetBackgroundColour("Black")
        horPanelSix = wx.Panel(self, pos=(0,310), size=(720,2))
        horPanelSix.SetBackgroundColour("Black")
        horPanelSeven = wx.Panel(self, pos=(0,362), size=(720,2))
        horPanelSeven.SetBackgroundColour("Black")
        horPanelEight = wx.Panel(self, pos=(0,414), size=(720,2))
        horPanelEight.SetBackgroundColour("Black")
        horPanelNine = wx.Panel(self, pos=(0,466), size=(720,2))
        horPanelNine.SetBackgroundColour("Black")

######################################################################

        def onButtonWeek(event):
            print("Button Pressed")
            windowTwo = wx.MessageDialog(self, """20 hours in class\n25 hours to study/eat
                                            \nWith 10 classes in 5 days""")
            windowTwo.ShowModal()

        def onButton(event):
            print("Button Pressed")
            windowTwo = wx.MessageDialog(self, "4 hours in class\n5 hours to study/eat")
            windowTwo.ShowModal()

        button = wx.Button(panelOne, -1, "Weekly\nBreakdown" , pos=(0,0), size=(98,50))
        button.Bind(wx.EVT_BUTTON, onButtonWeek)
        button.SetBackgroundColour("Red")
        button = wx.Button(panelOne, -1, "Monday", pos=(102,0), size=(98,50))
        button.Bind(wx.EVT_BUTTON, onButton)
        button.SetBackgroundColour("Grey")
        buttonTwo = wx.Button(panelOne, -1, "Tuesday", pos=(202,0), size=(98,50))
        buttonTwo.Bind(wx.EVT_BUTTON, onButton)
        buttonTwo.SetBackgroundColour("Grey")
        buttonThree = wx.Button(panelOne, -1, "Wednesday", pos=(302,0), size=(98,50))
        buttonThree.Bind(wx.EVT_BUTTON, onButton)
        buttonThree.SetBackgroundColour("Grey")
        buttonFour = wx.Button(panelOne, -1, "Thursday", pos=(402,0), size=(98,50))
        buttonFour.Bind(wx.EVT_BUTTON, onButton)
        buttonFour.SetBackgroundColour("Grey")
        buttonFive = wx.Button(panelOne, -1, "Friday", pos=(502,0), size=(98,50))
        buttonFive.Bind(wx.EVT_BUTTON, onButton)
        buttonFive.SetBackgroundColour("Grey")

######################################################################

        mainMenu = wx.MenuBar()

        fileButton = wx.Menu()

        mainMenu.Append(fileButton, "&File")

        exitButton = fileButton.Append(wx.ID_EXIT,"&Exit\tCtrl-Q")

        aboutButton = fileButton.Append(-1, "&About\tCtrl-A")


###################################################################

        self.SetMenuBar(mainMenu)

##################################################################

        self.Bind(wx.EVT_MENU, self.quit, exitButton)
        self.Bind(wx.EVT_MENU, self.about, aboutButton)

##################################################################

    def about(self, e):
        message = wx.MessageDialog(self, "Timelines, saving the day")
        message.ShowModal()


    def quit(self, e):
        self.Close()

def main():

    app = wx.App()
    window = mainFrame(None)
    window.Show()
    window.Centre()

    app.MainLoop()





main()
