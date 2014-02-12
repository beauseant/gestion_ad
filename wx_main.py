#GUI Para el proyecto gestion_ad

import lib.gui as gui
import wx

def main():
    
    app = wx.App()
    gui.Frm_Principal (None)
    app.MainLoop()    


if __name__ == '__main__':
    main()

