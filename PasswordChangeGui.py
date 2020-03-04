# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

import gettext
_ = gettext.gettext

###########################################################################
## Class ChangePwdFrame
###########################################################################

class ChangePwdFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Endre passord"), pos = wx.DefaultPosition, size = wx.Size( 339,286 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL, name = u"Endre passord" )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        PasswordChangeBox = wx.BoxSizer( wx.VERTICAL )

        TopBox = wx.FlexGridSizer( 0, 2, 0, 0 )
        TopBox.SetFlexibleDirection( wx.BOTH )
        TopBox.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        TwoTextRows = wx.BoxSizer( wx.VERTICAL )

        TwoTextRows.SetMinSize( wx.Size( 220,-1 ) )
        self.TopAlertText = wx.StaticText( self, wx.ID_ANY, _(u"Du må endre passord nå"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TopAlertText.Wrap( -1 )

        self.TopAlertText.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.TopAlertText.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        TwoTextRows.Add( self.TopAlertText, 0, wx.ALL, 5 )

        self.TopErrorText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TopErrorText.Wrap( -1 )

        self.TopErrorText.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        TwoTextRows.Add( self.TopErrorText, 0, wx.ALL, 5 )


        TopBox.Add( TwoTextRows, 1, wx.EXPAND, 5 )

        self.logo = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        TopBox.Add( self.logo, 0, wx.ALL, 5 )


        PasswordChangeBox.Add( TopBox, 1, wx.EXPAND, 5 )

        form = wx.FlexGridSizer( 0, 2, 0, 0 )
        form.SetFlexibleDirection( wx.BOTH )
        form.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Gammelt passord"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        form.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.OldPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
        form.Add( self.OldPassword, 0, wx.ALL, 5 )

        self.NewPassword1Text = wx.StaticText( self, wx.ID_ANY, _(u"Nytt passord"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NewPassword1Text.Wrap( -1 )

        form.Add( self.NewPassword1Text, 0, wx.ALL, 5 )

        self.NewPassword1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        form.Add( self.NewPassword1, 0, wx.ALL|wx.EXPAND, 5 )

        self.NetPassword2Text = wx.StaticText( self, wx.ID_ANY, _(u"Gjenta nytt passord"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NetPassword2Text.Wrap( -1 )

        form.Add( self.NetPassword2Text, 0, wx.ALL, 5 )

        self.NewPassword2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        form.Add( self.NewPassword2, 0, wx.ALL|wx.EXPAND, 5 )

        self.ButtonChangePassword = wx.Button( self, wx.ID_ANY, _(u"Endre passord"), wx.DefaultPosition, wx.DefaultSize, 0 )
        form.Add( self.ButtonChangePassword, 0, wx.ALL, 5 )

        self.ButtonCancel = wx.Button( self, wx.ID_ANY, _(u"Tøm felter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        form.Add( self.ButtonCancel, 0, wx.ALL, 5 )


        PasswordChangeBox.Add( form, 1, wx.EXPAND, 5 )

        self.PasswordRulesLink = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, _(u"Passordregler"), u"http://opplaring.as-admin.no/palogging/passordregler/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
        PasswordChangeBox.Add( self.PasswordRulesLink, 0, wx.ALL, 5 )


        self.SetSizer( PasswordChangeBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.OldPassword.Bind( wx.EVT_KEY_DOWN, self.onEnter )
        self.ButtonChangePassword.Bind( wx.EVT_BUTTON, self.ChangePassword )
        self.ButtonCancel.Bind( wx.EVT_BUTTON, self.clearFunc )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onEnter( self, event ):
        event.Skip()

    def ChangePassword( self, event ):
        event.Skip()

    def clearFunc( self, event ):
        event.Skip()


###########################################################################
## Class SuccessDialog
###########################################################################

class SuccessDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 198,97 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.PasswordChangedText = wx.StaticText( self, wx.ID_ANY, _(u"Passordet ble endret"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PasswordChangedText.Wrap( -1 )

        self.PasswordChangedText.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer2.Add( self.PasswordChangedText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button4 = wx.Button( self, wx.ID_ANY, _(u"Ok"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button4.Bind( wx.EVT_BUTTON, self.onClose )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onClose( self, event ):
        event.Skip()


