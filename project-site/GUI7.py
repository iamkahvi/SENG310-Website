import wx


class mainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(mainFrame, self).__init__(*args, **kwargs)

        self.GUI()
        self.SetSize((618,575))

    def GUI(self):

###################################################################
# Area for creating functions for Buttons for GUI function
###################################################################

        def onButtonWeek(event):
            print("Button Pressed")
            windowTwo = wx.MessageDialog(self, """20 hours in class\n25 hours to study/eat
                                            \nWith 10 classes in 5 days""")
            windowTwo.ShowModal()

        def onButton(event):
            print("Button Pressed")
            windowTwo = wx.MessageDialog(self, "4 hours in class\n5 hours to study/eat")
            windowTwo.ShowModal()

        def onButtonDays(event):
            windowTwo=wx.MessageDialog(self, "ECE 330\nECE A123")
            windowTwo.ShowModal()

####################################################################
# Area to create panels
####################################################################

        panelOne = wx.Panel(self, pos=((0,0)), size=((618,575)))
        panelOne.SetBackgroundColour("White")
#        panelTwo = wx.Panel(self, pos=((0,52)), size=((618,50)))
#        panelTwo.SetBackgroundColour("White")
#        panelThree = wx.Panel(self, pos=((0,104)), size=((618,50)))
#        panelThree.SetBackgroundColour("White")
#        panelFour = wx.Panel(self, pos=((0,156)), size=((618,50)))
#        panelFour.SetBackgroundColour("White")
#        panelFive = wx.Panel(self, pos=((0,208)), size=((618,50)))
#        panelFive.SetBackgroundColour("White")
#        panelSix = wx.Panel(self, pos=((0,260)), size=((618,50)))
#        panelSix.SetBackgroundColour("White")
#        panelSeven = wx.Panel(self, pos=((0,312)), size=((618,50)))
#        panelSeven.SetBackgroundColour("White")
#        panelEight = wx.Panel(self, pos=((0,364)), size=((618,50)))
#        panelEight.SetBackgroundColour("White")
#        panelNine = wx.Panel(self, pos=((0,416)), size=((618,50)))
#        panelNine.SetBackgroundColour("White")
#        panelTen = wx.Panel(self, pos=((0,468)), size=((618,50)))
#        panelTen.SetBackgroundColour("White")

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
# Area to create the buttons for the top section of the schedule (week/day name
######################################################################

        buttonWeek = wx.Button(panelOne, -1, "Weekly\nBreakdown" , pos=(0,0), size=(98,50))
        buttonWeek.Bind(wx.EVT_BUTTON, onButtonWeek)
        buttonWeek.SetBackgroundColour("Red")
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
# Section for the function for the day buttons and the area to create them
######################################################################

        dayButton = wx.Button(panelOne, -1, "ECE 330\nECE A123", pos=(102,52), size=(98,50))
        dayButton.Bind(wx.EVT_BUTTON, onButtonDays)
        dayButton.SetBackgroundColour("Green")
        dayButtonTwo = wx.Button(panelOne, -1, "SENG-310\nELL A168", pos=(202,139), size=(98,67))
        dayButtonTwo.Bind(wx.EVT_BUTTON, onButtonDays)
        dayButtonTwo.SetBackgroundColour("Green")

#######################################################################
# area for creating menus and attaching buttons the those menus
#######################################################################

        mainMenu = wx.MenuBar()

        fileButton = wx.Menu()

        mainMenu.Append(fileButton, "&File")

        exitButton = fileButton.Append(wx.ID_EXIT,"&Exit\tCtrl-Q")

        aboutButton = fileButton.Append(-1, "&About\tCtrl-A")


###################################################################

        self.SetMenuBar(mainMenu)

###################################################################
# Area to bind button to their functions
###################################################################

        self.Bind(wx.EVT_MENU, self.quit, exitButton)
        self.Bind(wx.EVT_MENU, self.about, aboutButton)

###################################################################
# Area for static text in function GUI
####################################################################

        hourOne = wx.StaticText(panelOne, -1, "8:30-9:30", pos=(25, 70))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "9:30-10:30", pos=(25, 122))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "10:30-11:30", pos=(22, 174))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "11:30-12:30", pos=(22, 226))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "12:30-1:30", pos=(22, 278))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "1:30-2:30", pos=(25, 330))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "2:30-3:30", pos=(25, 382))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "3:30-4:30", pos=(25, 434))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")
        hourOne = wx.StaticText(panelOne, -1, "4:30-5:30", pos=(25, 486))
        hourOne.SetForegroundColour("Black")
        hourOne.SetBackgroundColour("Grey")

####################################################################
# Area for creating functions for Buttons for the class of mainFrame
####################################################################

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
