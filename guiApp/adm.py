#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Fri Feb 14 17:45:57 2014
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from Frm_Main import Frm_Main

class App_adm(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        initFrm = Frm_Main(None, wx.ID_ANY, "")
        self.SetTopWindow(initFrm)
        initFrm.Show()
        return 1

# end of class App_adm

if __name__ == "__main__":
    gettext.install("adm") # replace with the appropriate catalog name

    adm = App_adm(0)
    adm.MainLoop()