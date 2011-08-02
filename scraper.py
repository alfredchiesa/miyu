from BeautifulSoup import BeautifulSoup as BS
import urllib, urllib2, settings, cookielib

class Scraper():
    def __init__(self):
        """
        Initializes the scraper with all the proper attributes and information
        that is needed to successuly scrape.
        """
        values = {}
        self.data = urllib.urlencode(values)
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        self.opener.addheaders.append(('User-Agent', settings.USER_AGENT))
        self.opener.addheaders.append(('Referer', settings.REFERRER))
    
    def collect_manus(self, **kwargs):
        kind = kwargs.get('kind', 'china')
        if kind == 'china':
            for alpha in settings.MANU_CHINA_ALPHA:
                self.url = settings.MANU_CHINA_URL + "%s.htm" % alpha
                print self.url
                self.response = self.opener.open(self.url, self.data)
                self.response = self.response.read()
                self.pool = BeautifulSoup(self.response)
                print pool.findAll('div', attrs={'class':'inventory'})