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
        # now lets build a nice csv to store all this crud in
        self.csv = open("Results.csv", 'w')
        self.csv.write("Manufacturer, Product Type, Pattern Name, Pattern Number, Image\n")
    
    def collect_manus(self, **kwargs):
        """
        Get a big list of all the manufacturers and then go out and scrape their
        corresponding patterns.
        """
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
                            link = links.attrs[0][1].strip("../") if \
                            links.attrs[0][1] != "#top" or "../splash.htm" \
                            else "None"
                            brand = links.string
                            print "trying %s" % str(brand)
                            self.find_patterns(kind=kind, link=link, brand=brand)
                else:
                    print "can't work on '%s' for you at the moment" % alpha.upper
                    break
    
    def find_patterns(self, **kwargs):
        """
        This is the method that collects all the links form the manu page and sends
        them to be recorded in the CSV file.
        """
        kind = kwargs.get('kind', 'china')
        if kind == 'china':
            link = kwargs.get('link', 'None')
            brand = kwargs.get('brand', 'None')
            page = BS(requests.get(settings.PATT_CHINA_URL + link).content)
            patterns = page.findAll('a')
            for each in patterns:
                if "padding:0 15 0 0" in str(each):
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1] != "#top" or "../splash.htm" else "None"
                    print patLink
                #if "../webquote/" in str(each):
                #    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                #    != "#top" or "../splash.htm" else "None"
                #    patName = each.string
                #    print patName, patLink
            #crumbs = self.pattList.findAll('a', attrs={"style": "padding:0 15 0 0"})   
    
    def get_info(self, **kwargs):
        kind = kwargs.get('kind', 'china')
        patName = kwargs.get('patName', 'None')
        brand = kwargs.get('brand', 'None')
        link = kwargs.get('link', 'None')
        page = BS(requests.get(settings.ROOT_SITE + link).content)
        self.csv.write("%s, %s, %s, %s, %s\n" % ())
    
    def record_info(self, **kwargs):
        pass