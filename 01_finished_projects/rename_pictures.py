import os
import shutil

#renaming pictures - if folder name is brasil -> filenames: brasil_01 ; brasil_02 etc

path=input("Please enter now the path where the folders of the pictures are!:")

for folderName,subfolders,fNames in os.walk(path):
    counter=0
    for fname in fNames:
        current_folder=os.path.basename(folderName)
        os.rename(os.path.join(folderName,fname),os.path.join(folderName,current_folder+"_0"+str(counter)+".jpeg"))
        counter+=1