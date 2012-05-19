import urllib.request
import lxml.html
import openwifi

class AirportIAD(openwifi.Module):
    def login(self):
        doc = lxml.html.parse(self.login_page)
        form = doc.getroot().forms[0]
        form.fields['terms'] = 'checkbox'
        self.submit_form(form)
