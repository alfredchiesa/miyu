from BeautifulSoup import BeautifulSoup as BS
import urllib, urllib2, settings, cookielib, requests, re

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
        self.csv.write("Kind, Manufacturer, Pattern Name, Pattern Number, Item Number, Description\n")
        self.count = 0
    
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
        elif kind == "crystal":
            for alpha in settings.MANU_CRYSTAL_ALPHA:
                self.url = settings.MANU_CRYSTAL_URL + "%s.htm" % alpha
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
        elif kind == "silver":
            for alpha in settings.MANU_SILVER_ALPHA:
                self.url = settings.MANU_SILVER_URL + "%s.htm" % alpha
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
                patName = None
                patLink = None
                if "padding:0 15 0 0" in str(each):
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = "None"
                if "../webquote/" in str(each): 
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = each.string
                self.get_info(kind=kind, patName=patName, patLink=patLink, brand=brand)
        elif kind == "crystal":
            link = kwargs.get('link', 'None')
            brand = kwargs.get('brand', 'None')
            page = BS(requests.get(settings.PATT_CRYSTAL_URL + link).content)
            patterns = page.findAll('a')
            for each in patterns:
                patName = None
                patLink = None
                if "padding:0 15 0 0" in str(each):
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = "None"
                if "../webquote/" in str(each): 
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = each.string
                self.get_info(kind=kind, patName=patName, patLink=patLink, brand=brand)
        elif kind == "silver":
            link = kwargs.get('link', 'None')
            brand = kwargs.get('brand', 'None')
            page = BS(requests.get(settings.PATT_SILVER_URL + link).content)
            patterns = page.findAll('a')
            for each in patterns:
                patName = None
                patLink = None
                if "padding:0 15 0 0" in str(each):
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = "None"
                if "../webquote/" in str(each): 
                    patLink = each.attrs[0][1].strip("../") if each.attrs[0][1]\
                    != "#top" or "../splash.htm" else "None"
                    patName = each.string
                self.get_info(kind=kind, patName=patName, patLink=patLink, brand=brand)
    
    def get_info(self, **kwargs):
        kind = kwargs.get('kind', 'china')
        patName = kwargs.get('patName', None)
        brand = kwargs.get('brand', None)
        link = kwargs.get('patLink', None)
        if link:
            page = BS(requests.get(settings.ROOT_SITE + link).content)
            # try and get the item number
            itemRegex = re.compile(r"<font color=\"#FF0000\">(.+?)</font>", re.I)
            try:
                result = re.search(itemRegex, str(page))
                itemNumber = result.group(0).replace("<font color=\"#FF0000\">", '').replace(" ", '').replace("</font>", '')
            except:
                itemNumber = "n/a"
            #try and get the pattern number
            nameRegex = re.compile(r"Pattern #:(.+?)</H1>", re.I)
            try:
                result = re.search(nameRegex, str(page))
                patNum = result.group(0).replace("Pattern #:", '').replace(" ", '').replace("</H1>", '').replace("</h1>", '')
            except:
                patNum = "n/a"
            # try and get the description
            desRegex = re.compile(r"Description:(.+?)</b>", re.I)
            try:
                result = re.search(desRegex, str(page))
                desc = result.group(0).replace("Description:", '').replace("</b>", '')
            except:
                desc = "n/a"
            self.count = self.count +1
            print "found %s patterns so far" % str(self.count)
            self.csv.write("%s, %s, %s, %s, %s, %s\n" % (str(kind), str(brand), str(patName), str(patNum), str(itemNumber), str(desc)))
    def record_info(self, **kwargs):
        pass