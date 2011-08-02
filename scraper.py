from BeautifulSoup import BeautifulSoup as BS
import urllib, urllib2, settings, cookielib, requests

class Scraper():
    def __init__(self):
        """
        Initializes the scraper with all the proper attributes and information
        that is needed to successuly scrape.
        """
        values = {}
        self.data = urllib.urlencode(values)
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.opener.addheaders.append(('User-Agent', settings.USER_AGENT))
        self.opener.addheaders.append(('Referer', settings.REFERRER))
    
    def collect_manus(self, **kwargs):
        kind = kwargs.get('kind', 'china')
        if kind == 'china':
            for alpha in settings.MANU_CHINA_ALPHA:
                self.url = settings.MANU_CHINA_URL + "%s.htm" % alpha
                self.response = requests.get(self.url)
                if int(self.response.status_code) <= 200:
                    self.pool = BS(self.response.content)
                    results = self.pool.findAll('td', attrs={"width": "50%"})
                    for each in results:
                        for links in each.findAll('a'):
                            link = links.attrs[0][1] if links.attrs[0][1] != \
                            "#top" or "../splash.htm" else "None"
                            brand = links.string
                            print brand, link
                else:
                    print "can't work on '%s' for you at the moment" % alpha.upper
                    break
    
    def find_patterns(self, **kwargs):
        pass