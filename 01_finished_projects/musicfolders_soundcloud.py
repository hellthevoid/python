import os
import shutil

#Creates artist folder in Soulseek complete folder

#path=input("Please enter now the path where the music is!:")
path=os.getcwd()

def create_album_folders(path):
    for folderNames,subfolders,fNames in os.walk(path):
        for fname in fNames:
            if "-" in fname:
                name=fname.split(".mp")
                destination=os.path.join(path,name[0])
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.move(os.path.join(path,fname),destination)#move folder into new folder
        return 0 # stop after the files in the main folder

def create_artist_folder(path):
    for folderNames,subfolders,fNames in os.walk(path):
        
        for folder in subfolders:
            if "-" in folder:
                name=folder.split(' -')
                destination=os.path.join(path,name[0])
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.move(os.path.join(path,folder),destination)#move folder into new folder


create_album_folders(path)

create_artist_folder(path)

