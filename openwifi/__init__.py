import urllib.request

class Module(object):
    test_url = 'http://www.google.com/'
    user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 "\
            "Firefox/12.0"

    def __init__(self):
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [
            ('User-agent', self.user_agent),
        ]

        resp = self.opener.open(self.test_url)
        if resp.geturl() != self.test_url:
            self.login(resp)
            print("Connected.")
        else:
            print("You are already connected.")
