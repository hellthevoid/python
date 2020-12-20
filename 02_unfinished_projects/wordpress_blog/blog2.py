"""Wordpress.com blog scraper v1.0
Should work on majority of wp blogs,
will scrape text and images and save
to a folder with blogs name.

By Steve Shambles 2018
updated nov 2019.

stevepython.wordpress.com

pip3 install beautifulsoup4
pip3 install requests
"""
import os
import re
from urllib.request import urlopen
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
import requests

BLOG2_SCRAPE = ''
POSTLINK = ''

def scrape_link():
    """Get the text body and images of links."""
    ht_ml = urlopen(POSTLINK)
    b_s = BeautifulSoup(ht_ml.read(), 'lxml')

    for article in b_s.find_all(class_="post*"):
        pass


POSTLINK = 'https://ntoverland.wordpress.com/2017/06/27/beaucheff/'
scrape_link()

print()
print()
print("Finished Scrape.")
