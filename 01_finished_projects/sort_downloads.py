import os
import shutil

#move files of the download folder to certain destinations

def move_type(path,file_type,destination):
    if not os.path.exists(path+destination):
        dir_doc=os.makedirs(destination)

    for folderName,subfolders,f_names in os.walk(path):
        for f_name in f_names:
            if f_name.endswith(file_type):
                try:
                    shutil.move(os.path.join(folderName,f_name),destination)
                except Exception:
                    pass

path="C:\\Users\\sonyx\\Downloads"
os.chdir(path)

type_dic={".pdf":".\\d_documents",".docx":".\\d_documents",".exe":".\\d_executables",
".rar":".\\d_zips",".zip":".\\d_zips",".jpeg":".\\d_images"}

for file_type, destination in type_dic.items():
    move_type(path,file_type,destination)
        