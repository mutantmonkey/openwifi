import urllib.request
import lxml.html
import openwifi

class AirportDEN(openwifi.Module):
    def login(self):
        doc = lxml.html.parse(self.login_page)
        form = doc.getroot().forms[0]
        form.fields['agree'] = ''
        form.fields['accept'] = "Continue"
        self.submit_form(form)
