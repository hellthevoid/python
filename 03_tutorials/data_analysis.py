import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df=pd.read_csv(path,header=None)

#print(df)

df_head=df.head()
df_tails=df.tail(10)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
"num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
"peak-rpm","city-mpg","highway-mpg","price"]

#header
df.columns=headers

#df.to_excel("pandas.xls")
#print(df_head)

#datatypes
df.dtypes

#stats insights
df.describe(include="all")

#choose certain columns
df[["make","city-mpg"]]

print(df[["make","city-mpg"]].describe(include="all"))



x=np.linspace(0,50,50)
y=np.linspace(1000,20000,50)

#fig=plt.figure()

df=pd.DataFrame(x,y)

print(df.head())


#plt.plot(x,y)
#plt.show()
