# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Fri Feb 14 17:06:48 2014
#

import wx
import sys

sys.path.append('..')
import lib.gestionUsuarios as ad
import lib.db as db_c

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade







class Frm_NewConn(wx.Frame):
    def __init__(self, *args, **kwds):

	self._gdb = ''
	

        # begin wxGlade: Frm_NewConn.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.connections_title_label = wx.StaticText(self, -1, _("Connections Properties"))
        self.configurations_combo_label = wx.StaticText(self, -1, _("Saved configurations"))
        self.configurations_combo = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.new_configuration_label = wx.StaticText(self, -1, _("New configuration"))
        self.inst_new_configuration_label = wx.StaticText(self, -1, _("Introduce the connection data"))
        self.txt_server_label = wx.StaticText(self, -1, _("Server"))
        self.txt_server = wx.TextCtrl(self, -1, "")
        self.txt_CN_label = wx.StaticText(self, -1, _("CN"))
        self.txt_CN = wx.TextCtrl(self, -1, "")
        self.txt_name_label = wx.StaticText(self, -1, _("Name"))
        self.text_name = wx.TextCtrl(self, -1, "")
        self.txt_passwd_label = wx.StaticText(self, -1, _("Password"))
        self.txt_passwd = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.btn_save = wx.Button(self, -1, _("Save configuration"))
        self.btn_ok = wx.Button(self, -1, _("OK"))
        self.btn_cancel = wx.Button(self, -1, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.cmbox_Click, self.configurations_combo)
        self.Bind(wx.EVT_BUTTON, self.btn_save_Click, self.btn_save)
        self.Bind(wx.EVT_BUTTON, self.btn_ok_Click, self.btn_ok)
        self.Bind(wx.EVT_BUTTON, self.btn_cancel_Click, self.btn_cancel)
        # end wxGlade
        
        self._gdb = db_c.db ('./')
        self.parent = kwds['parent']

	#Cargamos configuraciones de la base de datos:
	self.loadComboBox ()
	#Seleccionamos la primera:
	self.configurations_combo.SetSelection ( 0 )
	#Y actualizamos valores de las etiquetas:
	self.cmbox_Click ('')


    def __set_properties(self):
        # begin wxGlade: Frm_NewConn.__set_properties
        self.SetTitle(_("New connection"))
        self.connections_title_label.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.configurations_combo_label.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.configurations_combo.SetFocus()
        self.new_configuration_label.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.inst_new_configuration_label.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frm_NewConn.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.FlexGridSizer(6, 2, 0, 0)
        sizer_8.Add(self.connections_title_label, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 15)
        grid_sizer_2.Add(self.configurations_combo_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.configurations_combo, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.new_configuration_label, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.inst_new_configuration_label, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 13)
        grid_sizer_2.Add(self.txt_server_label, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.txt_server, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.txt_CN_label, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.txt_CN, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.txt_name_label, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.text_name, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.txt_passwd_label, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 15)
        grid_sizer_2.Add(self.txt_passwd, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.AddGrowableRow(0)
        grid_sizer_2.AddGrowableRow(2)
        grid_sizer_2.AddGrowableRow(3)
        grid_sizer_2.AddGrowableRow(4)
        grid_sizer_2.AddGrowableRow(5)
        grid_sizer_2.AddGrowableCol(1)
        sizer_8.Add(grid_sizer_2, 1, wx.ALL|wx.EXPAND, 20)
        sizer_9.Add(self.btn_save, 0, wx.ADJUST_MINSIZE, 0)
        sizer_9.Add(self.btn_ok, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 100)
        sizer_9.Add(self.btn_cancel, 0, wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 80)
        sizer_8.Add(sizer_9, 0, wx.ALL|wx.ADJUST_MINSIZE, 15)
        sizer_7.Add(sizer_8, 1, wx.ALL|wx.EXPAND, 20)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    #Cerramos la ventana sin hacer nada:
    def btn_cancel_Click(self, event):  # wxGlade: Frm_NewConn.<event_handler>
        self.MakeModal(False)
        self.Destroy()
        event.Skip()
    def btn_ok_Click(self, event):  # wxGlade: Frm_NewConn.<event_handler>
        #Recopilamos toda la información introducida por el usuario, comprobamos que esta todo correcto e intentamos lanzar una conexion:
        self.parent.__server    = self.txt_server.GetValue ()
        self.parent.__CN        = self.txt_CN.GetValue ()
	self.parent.__user	= self.text_name.GetValue()
        self.parent.__passwd    = self.txt_passwd.GetValue ()
        
        if ( ( not self.parent.__server ) or ( not self.parent.__CN ) or ( not self.parent.__passwd ) or ( not self.parent.__user )) :
            dlg = wx.MessageDialog(self, message='Please, fill in all the blanks.', caption='error:',style=wx.ICON_ERROR )
            result = dlg.ShowModal() 
            dlg.Destroy() 
        else:                   
            if ( self.parent.__connectToServer () == 0 ):
                dlg = wx.MessageDialog(self, message='Connect error, check data', caption='error:',style=wx.ICON_ERROR )
                result = dlg.ShowModal() 
                dlg.Destroy()
            else:
                self.MakeModal(False)
                self.Destroy()


    def cmbox_Click(self, event): # wxGlade: Frm_NewConn.<event_handler>
	self.parent.__confname	= self.configurations_combo.GetValue()           

	configuration = self._gdb.recoverConnectionConfiguration(self.parent.__confname)
	self.txt_server.SetValue(configuration[1])
        self.txt_CN.SetValue(configuration[2])
        self.text_name.SetValue(configuration[3])


    def btn_save_Click(self, event): # wxGlade: Frm_NewConn.<event_handler>

        self.parent.__server    = self.txt_server.GetValue ()
        self.parent.__CN        = self.txt_CN.GetValue ()
        self.parent.__user      = self.text_name.GetValue()
        self.parent.__passwd    = self.txt_passwd.GetValue ()
        self.parent.__confname  = self.configurations_combo.GetValue()


        if ( ( not self.parent.__server ) or ( not self.parent.__CN ) or ( not self.parent.__passwd ) or ( not self.parent.__user ) or ( not self.parent.__confname )) :
            dlg = wx.MessageDialog(self, message='Please, fill in all the blanks.', caption='error:',style=wx.ICON_ERROR )
            result = dlg.ShowModal() 
            dlg.Destroy() 
        else:                   
            self._gdb.createConnectionsTable()
            self._gdb.saveConnectionConfiguration ( self.parent.__confname, self.parent.__server , self.parent.__CN, self.parent.__user)
	    self.configurations_combo.Append ( self.parent.__confname )
            dlg = wx.MessageDialog(self, message='Configuration saved.', caption='Succesful operation', style=wx.ICON_INFORMATION)
            result = dlg.ShowModal() 
            dlg.Destroy()


    def loadComboBox ( self ): # wxGlade: Frm_NewConn.<event_handler>
	configurations = self._gdb.recoverAllConfigurations()

	confs=[]
	for c in configurations:
		confs.append (str(c[0]))
		self.configurations_combo.Append ( c[0] )

	#return confs
	
	#self.configurations_combo = wx.ComboBox(self, -1, choices=confs, style=wx.CB_DROPDOWN)

# end of class Frm_NewConn
