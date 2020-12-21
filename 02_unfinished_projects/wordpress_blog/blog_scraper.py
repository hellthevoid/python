from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re

#import win32com.client
from docx import Document
from htmldocx import HtmlToDocx
import sys
import linecache

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))




def docx_replace_regex(doc_obj, regex , replace,regex_left):
    '''searches a document (doc_obj) and locates regex,
    and replaces it with replace.  doc_obj passed by reference
    so no need to return it.
    '''
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text, count=1 )
                    inline[i].text = text
                    regex_left=True
                    return regex_left
    regex_left=False
    return regex_left

def delay():
    time.sleep(random.uniform(1,2))

def set_up_driver(link):
    driver=webdriver.Firefox()
    #driver.switch_to.window(driver.current_window_handle)
    #driver.minimize_window()
    try:
        driver.get(link)
    except Exception as e:
        driver.quit()
        time.sleep(200)
        driver=set_up_driver()
    
    return driver

def get_attributes(driver,month,document):

    actions=ActionChains(driver)

    try:
        widget= WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slide-menu-toggle"]'))
        )
    except Exception as e:
        print(e)
        return print("Error")

    actions.move_to_element(widget)
    actions.perform()
    
    delay()

    actions.click()
    actions.perform()

    delay()
    
    try:
        archive = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="archives-2"]'))
        )
    except Exception as e:
        print(e)
        return print("Error")

    try:
        menu = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slide-menu"]/h2'))
        )
    except Exception as e:
        print(e)
        return print("Error")

    webmonths=archive.find_elements_by_tag_name('a')

    for webmonth in webmonths:
        if webmonth.text==month:

            #actions.move_to_element(menu)
            #actions.perform()

            delay()
            link=webmonth.get_attribute('href')
    driver.get(link)

    delay()

    #add header
    try:
        header = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header'))
        )
    except Exception as e:
        print(e)
        return print("Error")

    try:
        new_parser = HtmlToDocx()
        header=header.get_attribute("innerHTML")
        new_parser.add_html_to_document(header, document)
    except Exception:
        pass

    '''
    try:
        article = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'site-main'))
        )
    except Exception as e:
        print(e)
        return print("Error")
    '''

    #add articles in reversed order
    articles=driver.find_elements_by_class_name("entry-content")
    articles=list(reversed(articles))

    articles_header=driver.find_elements_by_class_name("entry-header")
    articles_header=list(reversed(articles_header))

    counter=0 

    for article in articles:

        article=article.get_attribute("outerHTML") #Article content HTML
        
        #remove these parts from the html as they only cause problems e.g. smileys
        article=re.sub(r'<img draggable="false" role="img" class="emoji".*.svg">',"CAWABUNGA1",article)
        article1=re.sub(r'<div class="tiled-gallery type-rectangular" (.)*extra="{&quot;blog_id&quot;:115705291,&quot;permalink&quot;:&quot;https:\/\/ntoverland.wordpress.com\/2016\/11\/09\/you-better-belize-it\/&quot;,&quot;likes_blog_id&quot;:115705291}" itemscope="" (.)* <!-- close row --> </div>','test2',article)
        if article!=article1:
            print('something was changed')
        article=article1

        article_header=articles_header[counter].get_attribute("innerHTML") #Article Header HTML
        counter=counter+1

        #try:
        new_parser = HtmlToDocx()
        new_parser.add_html_to_document(article_header, document)

        new_parser = HtmlToDocx()
        new_parser.add_html_to_document(article, document)
        #except Exception:
        #    print(article_header)
        #    PrintException()
    


    return driver,document


##MAIN##
document = Document()

months=['Juni 2017','Mai 2017','April 2017','März 2017','Februar 2017','Januar 2017','Dezember 2016','November 2016','Oktober 2016','September 2016','August 2016']
months=list(reversed(months))

driver=set_up_driver('https://ntoverland.wordpress.com/')

new_parser = HtmlToDocx()

for month in months:
    driver, document=get_attributes(driver,month,document)
    print("{} is done".format(month))
    document.save("ntoverland.docx")

#remove all links
regex = re.compile(r"(<link:.*/>)")
replace="CAWABUNGA"

regex_left=True
while regex_left==True:
    regex_left=docx_replace_regex(document,regex,replace,regex_left)

document.save("ntoverland1.docx")


