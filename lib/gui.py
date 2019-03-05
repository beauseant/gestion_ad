import wx


class Frm_Principal (wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Frm_Principal, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
        self.Centre()
        self.Show()
        
    def InitUI(self):    



        #La pantalla principal:
        panelPrinc = wx.Panel(self)
        
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        #Color de fondo de la pantalla inicial
        panelPrinc.SetBackgroundColour('#4f5049')
        
        
        
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panelPrinc)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panelPrinc.SetSizer(vbox)
        
        #panelPrinc = wx.Panel(self, -1)
        
        menubar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()

        
        
        self.shst = viewMenu.Append(wx.ID_ANY, 'Show name', 
            'Show the name', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show date', 
            'Show de date', kind=wx.ITEM_CHECK)
        
        fitem = fileMenu.Append(wx.ID_NEW , '&New connection...', 'create new connect to AD')
        fileMenu.AppendSeparator()
        fitem = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Quit application')
        

            
        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        #self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        #self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        #self.toolbar = self.CreateToolBar()
        #self.toolbar.AddLabelTool(1, '', wx.Bitmap('texit.png'))
        #self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((650, 550))
        self.SetTitle('Active Directory Management')
        self.Centre()
        self.Show(True)
        
        
        wx.TextCtrl(self)
        
        
        
        
    def ToggleStatusBar(self, e):
        
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

#    def ToggleToolBar(self, e):
#        
#        if self.shtl.IsChecked():
#            self.toolbar.Show()
#        else:
#            self.toolbar.Hide()        


    def OnCloseWindow(self, e):
    
            dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                
            ret = dial.ShowModal()
            
            if ret == wx.ID_YES:
                self.Destroy()
            else:
                e.Veto()