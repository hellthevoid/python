
import numpy as np
from itertools import cycle
from lxml.html import fromstring
from proxy_requests import ProxyRequests
import time
import music_database as MD
import pandas as pd
import rym_tags
from selenium import webdriver
from pathlib import Path
import random
import shutil
from datetime import date, datetime
import linecache
import sys
from tabulate import tabulate

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))



def set_up_rym_driver():
    driver=webdriver.Firefox()
    #driver.switch_to.window(driver.current_window_handle)
    driver.minimize_window()
    try:
        driver.get('https://rateyourmusic.com')
    except Exception as e:
        driver.quit()
        time.sleep(200)
        driver=set_up_rym_driver()
    rym_tags.delay()
    return driver

###Main###
today = str(datetime.now())
today=today.replace(':','-')

src_path_base='D:\\Musik\\Soundperlen\\'
dest_desktop="C:\\Users\\sonyx\\Desktop\\moodmusic\\"

#df=pd.read_csv('C:\\Users\\sonyx\\python\\music_database.csv',delimiter=',')

df=MD.read_db('music_database.csv')

#schreibe tags in database
#suche nur nach tags wenn noch nicht eingetragen

err_counter=0
album_counter=0

MD.create_all_shortcuts()

##############
df=MD.compare_db()
###############

################
#MD.decision_time(df)
#################

driver=set_up_rym_driver()

while 1:
    if err_counter>2:
            print('Album Counter:' + str(album_counter))
            #time.sleep(random.uniform(3550,3700))
            err_counter=0
            driver=set_up_rym_driver()

            MD.decision_time(df)
            
    artist, album, genre, row,complete_album=MD.get_rand(df) #get random album from database

    src_path = "{0}{1}\\{2}\\{3}".format(src_path_base, genre,artist, complete_album) #get album source directory

    try: #if error occurs reload website and try again
        tags,genres,year,rating,sr1,sr2,sr3=rym_tags.get_attributes(driver, artist=artist,album=album) #get tags

        if rating=='err_sel':
            raise Exception('Err_sel')
        
        df=MD.write_attributes(df,row,tags,genres,year,rating,sr1,sr2,sr3) #write tags into database

        MD.save_df('music_database.csv',df)

        #create shortcuts if the search result were not bad
        if not rating=='bad search result':
            
            [MD.create_shortcut(dest_desktop,src_path,complete_album,tag) for tag in tags] #create shortcut for each tag of an album
            print("Shortcut for {} created".format(complete_album))
            err_counter=0 #reset error counter is shortcut was successfull
        else:
            pass
            
            #driver.quit()
            #rym_tags.delay()
            #driver=set_up_rym_driver()
            print('bad result')


    except Exception:
        driver.quit()
        err_counter=err_counter+1
        PrintException()
        rym_tags.delay()
        driver=set_up_rym_driver()
        print('resetting driver because of error')

        pass
    time.sleep(random.uniform(10,20)) #dont overload website!
    album_counter=album_counter+1
