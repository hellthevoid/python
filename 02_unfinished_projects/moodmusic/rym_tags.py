from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random
import requests
from lxml.html import fromstring
import json

def err_sel():
    tags=['err_sel']*5
    genres=['err_sel']*3
    year='err_sel'
    rating='err_sel'
    sr1='err_sel'
    sr2='err_sel'
    sr3='err_sel'
    print('err_sel')

    return tags,genres,year,rating,sr1,sr2,sr3

def delay():
    time.sleep(random.uniform(1,2))

def bad_search_result(driver,sr1,sr2,sr3):

    tags=['bad search result']*5
    genres=['bad search result']*3
    year='bad search result'
    rating='bad search result'
   
    #first three search results
    sr1=sr1
    sr2=sr2
    sr3=sr3

    print('bad search result')

    return tags,genres,year,rating,sr1,sr2,sr3

def get_attributes(driver,artist,album):

    try:
        actions=ActionChains(driver)

        try:
            search_options = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'search_options_frame'))
            )
        except Exception as e:
            print(e)
            return err_sel()

        actions.move_to_element(search_options)
        actions.perform()
      
        delay()

        try:
            all_releases = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'searchtype_l'))
            )
        except Exception as e:
            print(e)
            return err_sel()

        #all_releases=driver.find_element_by_id()

        delay()

        actions.move_to_element(all_releases)
        actions.perform()

        delay()

        actions.click()
        actions.perform()

        try:
            search_bar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'mainsearch'))
            )
        except Exception as e:
            print(e)
            return err_sel()

        search_bar=search_bar.find_element_by_name('searchterm')

        time.sleep(random.uniform(1,3))

        search_bar.clear()
        search_bar.send_keys(artist+' '+album)
        time.sleep(random.uniform(1,2))
        search_bar.send_keys(Keys.ENTER)
        delay()
        delay()
        #get album name link
        try:
            search_results = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, 'searchresults'))
            )
        except Exception as e:
            print(e)
            return err_sel()
        time.sleep(random.uniform(3,6))
        info_boxes=search_results.find_elements_by_class_name('infobox')
        found_album=False
        #check each search result
        search_result_counter=0
        for info_box in info_boxes:
            search_result_counter+=1
            search_result_album=info_box.find_element_by_class_name('searchpage')
            search_result_album=str(search_result_album.text).strip()
            search_result_artist =info_box.find_element_by_class_name('artist')
            search_result_artist=str(search_result_artist.text).strip()

            if search_result_counter==1:
                sr1=(search_result_artist,search_result_album)
            elif search_result_counter==2:
                sr2=(search_result_artist,search_result_album)
            elif search_result_counter==3:
                sr3=(search_result_artist,search_result_album)

            album=album.strip()
            artist=artist.strip()
            #print('Search Alumb: '+search_result_album)
            #print('Search Artist: '+search_result_artist)
            #print('Artist:'+artist)
            #print('Album:'+album)

            python_link = info_box.find_elements_by_link_text(search_result_album) #
            driver.execute_script("arguments[0].scrollIntoView();", python_link[0])
            time.sleep(random.uniform(0.2,1))

            if search_result_album.lower()==album.lower() and search_result_artist.lower()==artist.lower():
                found_album=True
                #python_link = info_box.find_element_by_link_text(search_result_album)  # Find Python link.
                if len(python_link)>1:
                    python_link[1].click()
                else:
                    python_link[0].click()
                delay()
                
                break

        if not found_album==True:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            return bad_search_result(driver,sr1,sr2,sr3)
        else:
            sr1=''
            sr2=''
            sr3=''
         #get average rating
        try:
            rating = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "avg_rating"))
            )
        except Exception as e:
            print(e)
            return err_sel()
        
        rating=str(rating.text)
        
        #if rating is too bad -> bad search results
        #if float(rating)<2.8:
        #    print('bad rating')
        #    return bad_search_result(driver,sr1,sr2,sr3)

        tags = driver.find_element_by_class_name('release_descriptors')
        str_tags=str(tags.text)
        tags=str_tags.split(', ')
        tags=[tag.replace('Descriptors','') for tag in tags]
        tags=[tag.strip() for tag in tags] #remove sapce beginning + end

        #TO DO
        #print("Len of tags: " + str(len(tags)))
        if len(tags)==1 and tags[0]=="":
           tags[0]=0
            
        while len(tags)<5:
            tags.append('0')
        
        tags=tags[:5]

        
        genres = driver.find_element_by_class_name("release_pri_genres")
        genres=str(genres.text)
        genres=genres.split(', ')
        
        while len(genres)<3:
            genres.append('0')
        
        genres=genres[:3]
        
        year = driver.find_element_by_class_name("album_info")
        year=year.find_elements_by_tag_name('b')[0]
        year=str(year.text)

        return tags,genres,year,rating,sr1,sr2,sr3

    except Exception as e:
        print(e)
        return err_sel()
