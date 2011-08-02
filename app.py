from BeautifulSoup import BeautifulSoup as BS
import urllib, urllib2


class Scraper():
    def __init__(self):
        """
        Initializes the scraper with all the proper attributes and information
        that is needed to successuly scrape.
        """
        headers = {"User-Agent": USER_AGENT}
        data = urllib.urlencode(values)
        url = "%s?&Make=%s&Model=%s&LocationID=%s" % (PP_URL, MAKE, MODEL, LOCATION)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        page_response = response.read()
        pool = BeautifulSoup(page_response)
        
        results = pool.findAll('div', attrs={'class':'inventory'})