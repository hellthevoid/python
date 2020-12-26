import csv
import openpyxl
import os
import sys
import numpy as np
import pandas as pd



print("Calculation is starting...")
#set folder of script to current working directory
file_path=os.path.realpath(__file__)
directory_path=os.path.dirname(file_path)
os.chdir(directory_path) 

#insert path of module to sys.path to access it from other modules
if directory_path not in sys.path:
    sys.path.insert(0, directory_path) 


#set path for data csv files
path=".\\data"


df=pd.read_csv(".\\data\\2plate-R3.csv")


#change headers of df
#remove time
#make own time index
df.columns=["kann weg","sensor2","sensor1","??"]


#print(len(df))
df=df.drop(["kann weg","??"],axis=1)
#print(df.columns)

time=pd.DataFrame(np.transpose(np.arange(0,len(df)/10,0.1)),columns=["time"])

#print(time)
df=df.set_index(time["time"])
#print(time.shape)
#print(df.shape)
#print(df.head())
#print(df.tail())

#df=df["sensor2"]
#print (df)
for rw in df.itertuples():
    #print( rw[0])
    #print( rw[1])
    
    if rw[1]=="true":
        print(rw[0])

"""

#reading all csv files in a folder and put them into excel file (+trimming)
curr_col=1
for folderName,subfolders,fNames in os.walk(path):
    
    for fname in fNames:
        with open(os.path.join(folderName,fname)) as f_obj:
            reader = csv.reader(f_obj, delimiter=',')
            for row_index, row in enumerate(reader):
                for col_index, col in enumerate(row):
                    if col_index!=0:
                        cell=data_sheet.cell(row_index+1,col_index+1+curr_col)
                        cell.value=col.strip() #remove start/end spaces
        curr_col+=2
"""
