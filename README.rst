****
Miyu
****
Miyu is a China Pattern scraper. It has the ability to scrape all the manufacturers, patterns and image links from one of the worlds largest online sellers.

:Info: See `github <https://github.com/alfredchiesa/miyu>`_ for the latest source.
:Author: Alfred Chiesa <alfred@villaroad.com>

Required Packages
=================
- `Python 2.6 <http://python.org/download/>`_

- The following python packages installed using easy_install. This is explained in the server setup portion of this document::

    django
    BeautifulSoup
    requests


Usage
-----
To scrape for ``China`` edit app.py to match the following before running::

    from scraper import Scraper
    a = Scraper()
    a.collect_manus(kind='china')

To scrape for ``Crystal`` edit app.py to match the following before running::

    from scraper import Scraper
    a = Scraper()
    a.collect_manus(kind='crystal')

To scrape for ``Silver`` edit app.py to match the following before running::

    from scraper import Scraper
    a = Scraper()
    a.collect_manus(kind='silver')
