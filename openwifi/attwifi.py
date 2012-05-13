import urllib.request
import lxml.html
import openwifi

class AttWifi(openwifi.Module):
    def login(resp):
        doc = lxml.html.parse(resp)
        form = doc.getroot().forms[0]

        form.fields['aupAgree'] = 1
        form.fields['connect'] = "Connect"
        lxml.html.submit_form(form)
