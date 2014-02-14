# -*- coding: utf-8 -*-
# generated by wxGlade HG on Fri Feb 14 10:57:18 2014

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class MyFrame2(wx.MDIChildFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame2.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.MDIChildFrame.__init__(self, *args, **kwds)
        self.label_12 = wx.StaticText(self, -1, "Connection Properties")
        self.label_13 = wx.StaticText(self, -1, "Introduce your connection information")
        self.label_14 = wx.StaticText(self, -1, "Server")
        self.text_ctrl_9 = wx.TextCtrl(self, -1, "")
        self.label_15 = wx.StaticText(self, -1, "CN")
        self.text_ctrl_10 = wx.TextCtrl(self, -1, "")
        self.label_16 = wx.StaticText(self, -1, "Password")
        self.text_ctrl_11 = wx.TextCtrl(self, -1, "")
        self.button_3 = wx.Button(self, -1, "OK")
        self.button_4 = wx.Button(self, -1, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame2.__set_properties
        self.SetTitle("frame_4")
        self.SetSize((526, 422))
        self.label_12.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
        self.label_13.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
        self.button_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
        self.button_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame2.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_4 = wx.GridSizer(4, 4, 10, 10)
        grid_sizer_5 = wx.GridSizer(5, 4, 20, 20)
        sizer_6.Add(self.label_12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(self.label_13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_14, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.text_ctrl_9, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_15, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.text_ctrl_10, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_16, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.text_ctrl_11, 0, wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(grid_sizer_5, 3, wx.EXPAND, 0)
        grid_sizer_4.Add(self.button_3, 0, wx.ALIGN_RIGHT|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.button_4, 0, wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 2, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

# end of class MyFrame2


