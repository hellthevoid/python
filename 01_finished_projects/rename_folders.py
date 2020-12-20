import os
import shutil

#renaming folders
path=input("Please enter now the path where the folders are!:")

for folderName,subfolders,fNames in os.walk(path):
    if folderName !=path:
        print(folderName)
        
        current_folder_name=os.path.basename(folderName) #only the folder name
        print(current_folder_name)
        
        dirName=os.path.dirname(folderName) #the directory path infront of folder name 
        print(dirName)
        string='Various - '
        
        if not string in current_folder_name:
            os.rename(folderName,dirName+'\\'+string+current_folder_name)


        
    