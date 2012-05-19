import urllib.request
import lxml.html
import openwifi

class AttWifi(openwifi.Module):
    def login(self):
        doc = lxml.html.parse(self.login_page)
        form = doc.getroot().forms[0]
        form.fields['aupAgree'] = 1
        form.fields['connect'] = "Connect"
        lxml.html.submit_form(form)
