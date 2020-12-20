import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df=pd.read_csv(filename,names=headers)

df.replace('?',np.nan,inplace=True)

missing_data=df.isnull()


print(missing_data.head())


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  

#get the mean, needs to be treated as a float first
mean_norm_loss=df['normalized-losses'].astype('float').mean()

print(mean_norm_loss)


df['normalized-losses'].replace(np.nan,mean_norm_loss,inplace=True)

