
import bs4
import os
import send2trash
import re

from bs4 import NavigableString,Tag
#os.chdir("C:\\Users\\sonyx\\Desktop\\Lena")

from bs4.diagnose import diagnose

exampleFile = open("Bestellungen verwalten - Amazon (2).htm")
soup = bs4.BeautifulSoup(exampleFile.read())



for br in soup.findAll('br'):
    next_s = br.nextSibling
    if not (next_s and isinstance(next_s,NavigableString)):
        continue
    next2_s = next_s.nextSibling
    if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
        text = str(next_s).strip()
        if text:
            print ("Found:", next_s)
