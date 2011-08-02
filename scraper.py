from BeautifulSoup import BeautifulSoup as BS
import urllib, urllib2, settings

class Scraper():
    def __init__(self):
        """
        Initializes the scraper with all the proper attributes and information
        that is needed to successuly scrape.
        """
        values = {}
        self.headers = {"User-Agent": settings.USER_AGENT}
        self.data = urllib.urlencode(values)
    
    def collect_manus(self, **kwargs):
        kind = kwargs.get('kind', 'china')
        if kind == 'china':
            for alpha in settings.MANU_CHINA_ALPHA:
                self.url = settings.MANU_CHINA_URL + "%s.html" % alpha
                print self.url
                self.request = urllib2.Request(self.url, self.data, self.headers)
                self.response = urllib2.urlopen(self.request)
                self.response = self.response.read()
                self.pool = BeautifulSoup(self.response)
                print pool.findAll('div', attrs={'class':'inventory'})