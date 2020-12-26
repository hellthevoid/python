
##### HOW TO WORK WITH FILES AND DIRECTORYS#######

import os

print(os.getcwd()) #current working directory

os.chdir("C:\\Users\\sonyx\\Desktop\\python") #change current working directory

os.path.join('C:\\Users\\asweigart', filename) #join directory and filename

os.rename("test.txt","tes1t.txt") #rename a file

print(os.getcwd())

try:
    os.makedirs(".\\photo") #create a new subfolder
except FileExistsError:
    print("File already exists")

path="C:\\Users\\sonyx\\Desktop\\python"

print (os.path.basename(path)) #returns filename of a path (or last part of a path)
print (os.path.dirname(path)) # returns everything infront of a filename

tuple_path=os.path.split(path) # creates a tuple of basename and dirname

print("######")
print (tuple_path[0]+"\n"+tuple_path[1])

print(os.listdir(path)) #lists all files in a directory

# Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.

# Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.

# Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

import shutil

path0="C:\\Users\\sonyx\\Desktop\\python\\lena.txt"
destination="C:\\Users\\sonyx\\Desktop\\python\\test"

shutil.copy(path0,destination) #copy a file to a new path
#copy file to a location and gets a new name
shutil.copy("C:\\Users\\sonyx\\Desktop\\python\\lena.txt","C:\\Users\\sonyx\\Desktop\\python\\test\\LENANEU")

#copy a whole folder as an backup
shutil.copytree("C:\\Users\\sonyx\\Desktop\\python","C:\\Users\\sonyx\\Desktop\\python_backup")

path2=""
shutil.move(path2,destination)#move a file (paths must exist)

import send2trash

#deletes files and folders, but puts it into recycle bin first
send2trash.send2trash(path2) 

filename="test.txt"

if filename.endswith('.txt'): #check if a file ends with a special extension
    print(filename)

#loop through every file in a folder 
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)


# The os.walk() function is passed a single string value: the path of a folder. You can use os.walk() in a for loop statement to walk a directory tree, much like how you can use the range() function to walk over a range of numbers. Unlike range(), the os.walk() function will return three values on each iteration through the loop:
# 1.A string of the current folder’s name

# 2.A list of strings of the folders in the current folder

# 3.A list of strings of the files in the current folder

# (By current folder, I mean the folder for the current iteration of the for loop. The current working directory of the program is not changed by os.walk().)