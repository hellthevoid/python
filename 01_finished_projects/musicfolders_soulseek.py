import os
import shutil

#Creates artist folder in Soulseek complete folder

#path=input("Please enter now the path where the music is!:")
path='C:\\Users\\sonyx\\Documents\\Soulseek Downloads\\complete'
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
