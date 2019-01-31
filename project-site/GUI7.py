import wx

#######################################################
# This frame is for adding an event on the edit menu
#######################################################
class eventAddFrame(wx.Frame):
    def __init__(self):
        super(eventAddFrame, self).__init__(None, title="Add an Event")

        self.GUI()
        self.SetSize((400,300))
        self.Centre()

    def GUI(self):
        panelOne = wx.Panel(self, pos=(0,0), size=(400, 300))

        horizontalBar = wx.MenuBar()

        fileMenu = wx.Menu()

        exitButton = fileMenu.Append(wx.ID_EXIT, "&Exit\tCtrl-Q")

        horizontalBar.Append(fileMenu, "&File")

        ############################################################
        # Bind the buttons to functions
        ############################################################

        self.Bind(wx.EVT_MENU, self.quit, exitButton)

        ############################################################
        # Set the menu bars, horizontal
        ############################################################

        self.SetMenuBar(horizontalBar)

    def quit(self, e):
        self.Close()
########################################################
# This frame is for the buttons inide the days
########################################################
class secondFrame(wx.Frame):
    def __init__(self):
        super(secondFrame, self).__init__(None, title="Day Breakdown")

        self.GUI()
        self.SetSize((400,300))
        self.Centre()

    def GUI(self):
        panelOne = wx.Panel(self, pos=(0,0), size=(400, 300))

        wx.TextCtrl(panelOne, pos=(5,5), size=(370, 230))

        horizontalBar = wx.MenuBar()

        fileMenu = wx.Menu()

        exitButton = fileMenu.Append(wx.ID_EXIT, "&Exit\tCtrl-Q")

        horizontalBar.Append(fileMenu, "&File")

        ############################################################
        # Bind the buttons to functions
        ############################################################

        self.Bind(wx.EVT_MENU, self.quit, exitButton)

        ############################################################
        # Set the menu bars, horizontal
        ############################################################

        self.SetMenuBar(horizontalBar)

    def quit(self, e):
        self.Close()
####################################################################
# Main class for the frame of the schedule
####################################################################

class mainFrame(wx.Frame):

    x=0
    y=0

    def __init__(self, *args, **kwargs):
        super(mainFrame, self).__init__(*args, **kwargs)

        self.GUI()
        self.SetSize((618,575))

    ###################################################################
    # Area for creating functions for Buttons for GUI function
    ###################################################################

    def onButtonWeek(self, event):
        print("Button Pressed")
        windowTwo = wx.MessageDialog(self, """20 hours in class\n25 hours to study/eat
            \nWith 10 classes in 5 days""")
        windowTwo.ShowModal()

    def onButton(self, event):
        print("Button Pressed")
        windowTwo = wx.MessageDialog(self, "4 hours in class\n5 hours to study/eat")
        windowTwo.ShowModal()

    def onButtonDays(self, event):
        print("Button Pressed")
        windowTwo = secondFrame()
        windowTwo.Show()

    ###################################################################
    # This function has all the cotents of the frame
    ###################################################################

    def GUI(self):

        #######################################################################
        # area for creating menus and attaching buttons the those menus
        #######################################################################

        mainMenu = wx.MenuBar()

        fileButton = wx.Menu()
        editButton = wx.Menu()

        mainMenu.Append(fileButton, "&File")
        mainMenu.Append(editButton, "&Edit")

        exitButton = fileButton.Append(wx.ID_EXIT,"&Exit\tCtrl-Q")
        addEvent = editButton.Append(-1, "&Add Event")

        aboutButton = fileButton.Append(-1, "&About\tCtrl-A")


        ###################################################################
        # Set the menu bars below
        ###################################################################

        self.SetMenuBar(mainMenu)

        ###################################################################
        # Area to bind button to their functions
        ###################################################################

        self.Bind(wx.EVT_MENU, self.quit, exitButton)
        self.Bind(wx.EVT_MENU, self.about, aboutButton)
        self.Bind(wx.EVT_MENU, self.addE, addEvent)

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
        buttonWeek.Bind(wx.EVT_BUTTON, self.onButtonWeek)
        buttonWeek.SetBackgroundColour("Red")
        button = wx.Button(panelOne, -1, "Monday", pos=(102,0), size=(98,50))
        button.Bind(wx.EVT_BUTTON, self.onButton)
        button.SetBackgroundColour("Grey")
        buttonTwo = wx.Button(panelOne, -1, "Tuesday", pos=(202,0), size=(98,50))
        buttonTwo.Bind(wx.EVT_BUTTON, self.onButton)
        buttonTwo.SetBackgroundColour("Grey")
        buttonThree = wx.Button(panelOne, -1, "Wednesday", pos=(302,0), size=(98,50))
        buttonThree.Bind(wx.EVT_BUTTON, self.onButton)
        buttonThree.SetBackgroundColour("Grey")
        buttonFour = wx.Button(panelOne, -1, "Thursday", pos=(402,0), size=(98,50))
        buttonFour.Bind(wx.EVT_BUTTON, self.onButton)
        buttonFour.SetBackgroundColour("Grey")
        buttonFive = wx.Button(panelOne, -1, "Friday", pos=(502,0), size=(98,50))
        buttonFive.Bind(wx.EVT_BUTTON, self.onButton)
        buttonFive.SetBackgroundColour("Grey")

        ######################################################################
        # Section the day buttons and the area to create them
        ######################################################################

        dayButton = wx.Button(panelOne, -1, "ECE 330\nECE A123", pos=(102,52), size=(98,50))
        dayButton.Bind(wx.EVT_BUTTON, self.onButtonDays)
        dayButton.SetBackgroundColour("Green")
        dayButtonTwo = wx.Button(panelOne, -1, "SENG-310\nELL A168", pos=(202,139), size=(98,67))
        dayButtonTwo.Bind(wx.EVT_BUTTON, self.onButtonDays)
        dayButtonTwo.SetBackgroundColour("Green")

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
        message = wx.MessageDialog(self, "About Timelines\n at Timelines, we are always saving the day")
        message.ShowModal()


    def quit(self, e):
        self.Close()

    def placeEvent(self):
        buttonAdd = wx.Button(panelOne, -1, eventName, pos=(x,y), size=(98,50))
        self.Bind(wx.EVT_MENU, self.placeEvent, buttonAdd)
        buttonAdd.SetBackgroundColour("Green")

    def addE(self, e):
        eventName = wx.TextEntryDialog(None, "What is the name of the event", "Event Name")
        eventName.ShowModal()
        eventTime = wx.TextEntryDialog(None, "What is the time of the event", "Event Time")
        eventTime.ShowModal()
        if eventTime == "9:30-10:20":
            x = 102
            y = 104
        self.placeEvent()


def main():

    app = wx.App()
    window = mainFrame(None)
    window.Show()
    window.Centre()
    app.MainLoop()


main()
