import urllib.request

class Module(object):
    test_url = 'http://www.google.com/'
    user_agent = "openwifi/0.1"

    def __init__(self):
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [
            ('User-agent', self.user_agent),
        ]

    def connected(self):
        resp = self.opener.open(self.test_url)
        self.login_page = resp
        return resp.geturl() != self.test_url
