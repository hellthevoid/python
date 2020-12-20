import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
import shutil
import os

def set_up_rym_driver():
    driver=webdriver.Firefox()
    #driver.switch_to.window(driver.current_window_handle)
    driver.minimize_window()
    try:
        driver.get('https://rateyourmusic.com/list/sonyx/my-top-100-albums-as-of-2020/')
    except Exception as e:
        driver.quit()
        time.sleep(200)
        driver=set_up_rym_driver()
    delay(2,5)
    return driver

def delay(start,end):
    time.sleep(random.uniform(start,end))

def get_img(image_url,filename):
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        path="02_unfinished_projects\\best 100 albums\\"+filename
        with open(path,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

##########MAIN##############

driver=set_up_rym_driver()

try:
    info_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'list_art'))
    )
except Exception as e:
    print(e)
    
index=1

while index<109:


    try:
        temp = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list_art"))
        )
    except Exception as e:
        print(e)
        driver=set_up_rym_driver()
        delay(10,15)
        index=index+1
        continue

    info_boxes=driver.find_elements_by_class_name('list_art')
    filename="cover{}.png".format(str(index).zfill(2))

    if os.path.exists(path="02_unfinished_projects\\best 100 albums\\"+filename):
        print("skipped: "+filename)
        index=index+1
        continue

    link=info_boxes[index-1].find_element_by_css_selector('a')
    linktxt=str(link.get_attribute('href'))
    driver.get(linktxt)
    time.sleep(random.uniform(0.2,1))

    try:
        cover = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "coverart_img"))
        )
    except Exception as e:
        print(e)
        driver=set_up_rym_driver()
        delay(10,15)
        index=index+1
        continue

    src = cover.get_attribute('src')
    get_img(src,filename)

    index=index+1

    delay(10,15)
    driver.back()
    delay(5,10)

driver.close

