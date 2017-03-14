# -*- coding: utf-8 -*-
import pyad.adquery
import pyad.adsearch
import pyad.aduser

import gettext
_ = gettext.gettext
import os
import datetime

class PasswordExpiry:
    #def _init__(self):
    def test(self):
        return 'foo';
    def get_user(self):
        username = os.getenv('username')
        domain = os.getenv('userdnsdomain')
        dn = pyad.adsearch.by_upn('%s@%s' % (username, domain))
        user = pyad.aduser.ADUser.from_dn(dn)
        return user
    def pwd_last_set(self):
        return self.get_user().get_password_last_set()
    # Get password last set time (datetime object)
    #password_last_set = user.get_password_last_set()

    def message(self, max_password_age, warning_days):
        #Get the time when password was last changed
        password_last_set = self.pwd_last_set()
        # Create a timedelta object from the max password age
        max_password_age_delta = datetime.timedelta(days=+max_password_age)
        # Find the password expiry (datetime object)
        password_expiry_date = password_last_set + max_password_age_delta
        # Find how long until expiry (timedelta object)
        password_remaining_life = password_expiry_date - datetime.datetime.now()
        # Extract days until expiry as integer
        password_expiry_days = password_remaining_life.days

        print password_expiry_days
        if password_expiry_days == 1:
            return _('Passordet går ut i morgen. Bytt det nå')
        elif password_expiry_days < 0:
            return _('Ditt passord utgår aldri. Bytt det gjerne likevel')
        elif password_expiry_days < 1:
            return _('Passordet går ut i dag. Bytt det umiddelbart')
        elif password_expiry_days < warning_days:
            return _('Passordet går ut om %s dager. Bytt det før det går ut') % password_expiry_days
        else:
            return ''

#print password_expiry_message(password_last_set, 180, 14)
#max_password_age = 180
#warning_days = 14
#msg = password_expiry_message(password_last_set, max_password_age, warning_days)
