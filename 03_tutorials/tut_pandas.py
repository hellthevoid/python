
"""A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). 
What differentiates the NumPy array from a Series, is that a Series can have axis idx, meaning it can be indexed by a label, instead of just a number location.
 It also doesn't need to hold numeric data, it can hold any arbitrary Python Object."""


import numpy as np 
import pandas as pd

from  numpy.random import randn

my_list=[2,35,5,5,5]

idx=[1,2,3,4,5]
np.random.seed(101)

sers=pd.Series(data=my_list,index=idx)

print (sers)

mtx=np.random.rand(5,4)

print(mtx)
#Dataframes

cols=["a","b","c","d"]
df=pd.DataFrame(mtx,index=idx,columns=cols)

print(df)


print(df["a"])

df[["a","b"]]

#DataFrame Columns are just Series

df["new"] = df["a"] + df["b"]

#only real change if inplace=true
df.drop("new",axis=1,inplace=True)

df.drop(1,axis=0) #drop row


df.loc[2]#selecting row

df.iloc[1] #by row by index

df.loc[[1,2],['a','b']]

#conditional selecting

df>0 #boolean matrix
df[df>0] #all values above 0

print(df[df["a"]>0.2])#all values in column a higher than 0.2

df[df["a"]>0.3]["b"] #think about it

data=df[(df["a"]>0.4)&(df["b"]<0.2)] #and
data=df[(df["a"]>0.4)|(df["b"]<0.2)] #or
print(data)

#set new index

df.reset_index()

newind = 'CA NY WY OR CO'.split()

df['States'] = newind

df.set_index('States',inplace=True)

#multi index

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

"""For index hierarchy we use df.loc[], 
if this was on the columns axis, you would just use normal bracket notation df[]. 
Calling one level of the index returns the sub-dataframe: """

df.loc["G1"]
df.loc['G1'].loc[1]
df.index.names = ['Group','Num']

print(df)


frame=df.xs('G1')

print(frame)
df.xs(['G1',1])
df.xs(1,level='Num')


