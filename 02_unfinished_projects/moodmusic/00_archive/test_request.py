
from bs4 import BeautifulSoup
import requests
import csv
import os
import numpy as np
import os, winshell
from win32com.client import Dispatch
from itertools import cycle
from lxml.html import fromstring
from proxy_requests import ProxyRequests
import time
from music_database import*
import pandas as pd
from fake_useragent import UserAgent

def get_proxies():
    #url = 'https://free-proxy-list.net/'
    url = 'https://www.us-proxy.org/'

    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxy='http://{}'.format(proxy)
            proxies.add(proxy)
    return proxies

def get_tags(url_complete):

    proxi=get_proxies()
    proxy_pool = cycle(proxi)
    proxi = next(proxy_pool)
    referer='https://google.com'
    source=''


#####referer previous website#####
    while(source=='' or source.status_code != '200'):
        try:
            delays = [10, 12,14,19]
            delay = np.random.choice(delays)

            user_agent=UserAgent().random
            #user_agent=get_random_ua()
            headers={'user-agent':user_agent,'referer':referer,'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            	'accept-encoding': 'gzip, deflate,br',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Upgrade-Insecure-Requests':'1'}
            #print(requests.head(url_complete))
            source = requests.get(url_complete,headers=headers,proxies={"http": proxi, "https": proxi},timeout=10)
            #source = requests.get(url_complete).text
            print(type(source))
            return source
           
        except Exception as e:
            
            print(e)
            #print(str(source.status_code))
            if type(source)==requests.models.Response:
                if source.status_code=='400':
                    url_complete = url_complete.replace('_', '-')
                    proxi = next(proxy_pool)
                    time.sleep(delay)
                    pass
            else:
                proxi = next(proxy_pool)
                time.sleep(delay)
                pass
            



print(get_tags("https://jpc.de"))


