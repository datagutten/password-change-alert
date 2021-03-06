# -*- coding: utf-8 -*-
# Build:
# pyinstaller --onefile --distpath c:\PythonBuild --noconsole --win-private-assemblies PasswordChange.py

import datetime
import gettext
import os
# import config file
import sys

import pythoncom
# importing wx files
import wx
import wx.adv
# win32 libraries for password change
from win32com import adsi

# import the GUI file
import PasswordChangeGui as gui
import config
from PasswordExpiry import PasswordExpiry

_ = gettext.gettext
PasswordExpiry = PasswordExpiry()

# Function to do the password change in AD
# https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch07s15.html

def change_password(username, old_password, new_password):
    domain = os.getenv('userdnsdomain')
    ads_obj = adsi.ADsGetObject("WinNT://%s/%s,user" % (domain, username))

    try:
        ads_obj.ChangePassword(old_password, new_password)
    except pythoncom.com_error as e:
            (hr, msg, exc, arg) = e.args
            # Give clearer error messages; avoid stack traces
            scode = exc[5]
            msg = exc[2]
            if scode == -0x7ff8f88b:  # 0x8007005
                return _('Brukeren din er sperret som følge av for mange forsøk med feil passord')
            elif scode == -0x7ff8ffaa:  # 0x80070056
                return _("Det gamle passordet er feil")
            elif scode == -2147022651:  # 0x800708c5
                return _("Passordet oppfyller ikke kravene.\nKontroller lengden,\npassordsammensetningen og krav til passordhistorie.")
            else:
                return _('%s (Feilkode %s)') % (msg, scode)


# inherit from the MainFrame created in wxFowmBuilder and create PasswordBox
class PasswordBox(gui.ChangePwdFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.ChangePwdFrame.__init__(self, parent)
        self.NewPassword1.MoveAfterInTabOrder(self.OldPassword)
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        logo_file = os.path.join(base_path, "logo.png")
        self.logo.SetBitmap(wx.Bitmap(logo_file, wx.BITMAP_TYPE_ANY))

        if config.link_text and config.link_url:
            self.PasswordRulesLink = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, _(config.link_text), config.link_url, wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
            self.PasswordChangeBox.Add( self.PasswordRulesLink, 0, wx.ALL, 5 )

        # import PasswordExpiry

        # if msg:
        #     self.TopAlertText.SetLabel(msg)

    # put a blank string in text when 'Clear' is clicked
    def clearFunc(self, event):
        self.OldPassword.SetValue(str(''))
        self.NewPassword1.SetValue(str(''))
        self.NewPassword2.SetValue(str(''))

    def ChangePassword(self, event):
        if self.NewPassword1.GetValue() == self.NewPassword2.GetValue():
            message = change_password(os.getenv('username'), self.OldPassword.GetValue(), self.NewPassword1.GetValue())
            if not message:
                # SuccessBox(None).Show(True)
                # self.PasswordChangeBox.hide()
                expiry = datetime.datetime.now() + datetime.timedelta(days=+config.max_password_age)
                expiry_string = _('Passordet ble endret og er gyldig til %s') % expiry.strftime('%d.%m.%Y %H:%M')
                self.TopErrorText.SetLabel(expiry_string)
                if(os.path.isfile(trigger_file)):
                    os.remove(trigger_file)
                self.Close()
            else:
                self.TopErrorText.SetLabel(message)
        else:
            self.TopErrorText.SetLabel('Passordene er ikke like')

# Box to be displayed when the password is successfully changed (not currently in use)
class SuccessBox(gui.SuccessDialog):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.SuccessDialog.__init__(self, parent)

    def onClose(self, event):
        self.Close()
        # gui.ChangePwdFrame.close()


if config.trigger_file_path:
    trigger_file = config.trigger_file_path % os.getenv('username')
    trigger_file_exists = os.path.isfile(trigger_file)
else:
    trigger_file_exists = False

if config.ignore_file_path:
    ignore_file_exists = os.path.isfile(config.ignore_file_path % os.getenv('username'))
else:
    ignore_file_exists = False

if 'trigger' in sys.argv:
    print('Trigger message')
    trigger_file_exists = True
    ignore_file_exists = False

msg = PasswordExpiry.message(config.max_password_age, config.warning_days)

if((ignore_file_exists is False) and
   (trigger_file_exists or len(msg) > 0)):
    # mandatory in wx, create an app, False stands for not deteriction stdin/stdout
    # refer manual for details
    app = wx.App(False)

    # create an object of PasswordBox
    frame = PasswordBox(None)
    if len(msg) > 0:
        splitmsg = msg.split('. ')
        frame.TopAlertText.SetLabel(splitmsg[0])
        frame.TopErrorText.SetLabel(splitmsg[1])
    # show the frame
    frame.Show(True)
    # start the applications
    app.MainLoop()

# Relevant xkcds when working with passwords:
# http://xkcd.com/936/
# http://xkcd.com/792/
# http://xkcd.com/538/
