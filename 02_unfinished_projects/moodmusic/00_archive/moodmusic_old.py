import os
import shutil
import bs4

#jedes album meiner sammlung durchgehen
    #nach album auf rateyourmusic suchen https://rateyourmusic.com/release/album/lou_reed/coney_island_baby/
    
    #grab descriptors
    #ordner mit mood anlegen
    #verknüfung zu dem album ordner in alle zugehörigen mood ordner legen

#beautiful soup
#


from bs4 import NavigableString,Tag
#os.chdir("C:\\Users\\sonyx\\Desktop\\Lena")

from bs4.diagnose import diagnose

exampleFile = open("Bestellungen verwalten - Amazon (2).html")
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


path=input("Please enter now the path where the music is!:")

for folderNames,subfolders,fNames in os.walk(path):
    
    for folder in subfolders:
        if "-" in folder:
            name=folder.split(' -')
            destination=os.path.join(path,name[0])
            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(os.path.join(path,folder),destination)#move folder into new folder


#find album on rateyour music and get first 5 tags.
# then create tag folders for moods and create a link to the albums
