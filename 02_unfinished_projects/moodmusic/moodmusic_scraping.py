
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


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
            #####edited####
            random_proxy=random_proxy[:-2]
            #####
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_proxy


def get_genres(url_complete,header):
    source = requests.get(url_complete)
    soup = BeautifulSoup(source, 'lxml')
    genres=[]
    match=soup.find('tr', class_="release_genres") #class is a keyword in python, thats why the underscore
    for item in match.find_all('meta'):
        genres.append(str(item.get('content')))

    print(genres)

    return genres

#TODO: nur die ersten 5 Tags DONE
#nicht als roboter erkannt werden (sleeper)
#fix def create shortcut DONE
#falls ip ok dann weiter versuchen


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
            headers={'user-agent':user_agent,'referer':referer,	'host': 'https://rateyourmusic.com','accept-language': 'en-US,en;q=0.9,de;q=0.8'}
            	#'accept-encoding': 'gzip, deflate,br',
                #'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                #'Upgrade-Insecure-Requests':'1'}
            #print(requests.head(url_complete))
            source = requests.get(url_complete,headers=headers,proxies={"http": proxi, "https": proxi},timeout=10)
            #source = requests.get(url_complete).text
            print(type(source))
           
        except Exception as e:
            
            print(e)
            #print(str(source.status_code))
            if type(source)==requests.models.Response:
                if source.status_code=='400':
                    url_complete = url_complete.replace('_', '-')
            else:
                proxi = next(proxy_pool)
                time.sleep(delay)
                pass

    #src=requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers',headers=headers).text
    
    #req = ProxyRequests(url_complete)
    #req.set_headers(headers)
    #req.get_with_headers()
    #src=req.request
        #except:
            #print(Exception)
            #proxy = next(proxy_pool)
    #print(src)


    soup = BeautifulSoup(source, 'lxml')
    print(soup.prettify)
    tags=[]
    match=soup.find('tr', class_="release_descriptors") #class is a keyword in python, thats why the underscore
    for index, item in enumerate(match.find_all('meta')):
        if index<6:
            tags.append(str(item.get('content')))

    print(tags)
    ##########################################
    #time.sleep(delay)

    return tags 


def create_shortcut(src_path,artist,album,tag):

    dest = "C:\\Users\\sonyx\\Desktop\\moodmusic\\{0}".format(tag) # path to where you want to put the .lnk
    if not os.path.exists(dest):
        os.makedirs(dest)

    shortcut_path = os.path.join(dest, '{0}.lnk'.format(album))

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = src_path

    shortcut.save()

###Main###

src_path_base='D:\\Musik\\Soundperlen\\Ambient\\'
url_base='https://rateyourmusic.com/release/album/'

df=pd.read_csv('music_database.csv')

#schreibe tags in database
#suche nur nach tags wenn noch nicht eingetragen

artist, album,row=get_rand(df)

print(artist)
print(album)

html_artist=artist.replace(" ","_")
html_artist=html_artist.lower()
html_album = album.replace(" ", "_")
html_album=html_album.lower()

url_complete = "{0}{1}/{2}/".format(url_base, html_artist, html_album)
###umlaute?####
url_complete = url_complete.replace('&', 'and')
print(url_complete)
src_path = "{0}{1}\\{2}".format(src_path_base, artist, album)


tags = get_tags(url_complete)

#df=write_tags(df,tags)

'''
for tag in tags:
                create_shortcut(src_path, artist, album, tag)
'''
#tags=['energetic','sad','drugs']

#with open('database.txt') as database:
#    database.write('{0},{1}\n'.format(folder,tags))


#for folderNames,subfolders,fNames in os.walk(src_path_base):
    
#    for folder in subfolders:
#        if "-" in folder:
#            artist=folderNames.split("\\")[-1]

#            album=folder

#            html_album=folder.split('-')
#            html_album=html_album[1]
#            html_album=html_album[1:]
