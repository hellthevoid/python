
import numpy as np
import pandas as pd


df = pd.DataFrame({'A': [1, 2, np.nan],
'B': [5, np.nan, np.nan],
'C': [1, 2, 3]})


print(df)

df.dropna() #drop all rows that have an NAN

df.dropna(axis = 1) #drop all columns that have an NAN

df.dropna(thresh = 2) #drop only those rows that have at least 2 NANs

#fill NAN values 
df.fillna(value = 'FILL VALUE')


#fill NAN values with a mean of the column values of A
df['A'].fillna(value = df['A'].mean())


# Create dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
       'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
       'Sales': [200, 120, 340, 124, 243, 350]}


df = pd.DataFrame(data)

# ** Now you can use the .groupby() method to 
# group rows together based off of a column name. 
# For instance let's group based off of Company. 
# This will create a DataFrameGroupBy object:**

df.groupby('Company')
 
# You can save this object as a new variable:
by_comp = df.groupby("Company")

print(by_comp) #doesnt show much, need to call methods on it to make sense

# And then call aggregate methods off the object:

_mean=by_comp.mean()

print(_mean)

df.groupby('Company').mean()
 
# More examples of aggregate methods:

by_comp.std()
by_comp.min()
by_comp.max()
by_comp.count()

#shows alot of statistics
by_comp.describe()
by_comp.describe().transpose()

#shows just the value GOOG
by_comp.describe().transpose()['GOOG']


#MERGING JOINING AND CONCATENATING



df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index = [0, 1, 2, 3])



df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index = [4, 5, 6, 7]) 



df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index = [8, 9, 10, 11])



# ## Concatenation
# 
# Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are concatenating on. You can use **pd.concat** and pass in a list of DataFrames to concatenate together:

pd.concat([df1, df2, df3])


pd.concat([df1, df2, df3],
          axis = 1)


# _____
# ## Example DataFrames


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})    


# ## Merging
# 
# The **merge** function allows you to merge DataFrames together using a similar logic as merging SQL Tables together.
#  For example:


pd.merge(left, right, 
         how = 'inner',
         on = 'key')


# Or to show a more complicated example:

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})



pd.merge(left, right, 
         on=['key1', 'key2'])


pd.merge(left, right, 
         how = 'outer', 
         on = ['key1', 'key2'])



pd.merge(left, right, 
         how = 'right', 
         on = ['key1', 'key2'])



pd.merge(left, right, 
         how = 'left', 
         on = ['key1', 'key2'])


# ## Joining
# Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a single result DataFrame.


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index = ['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index = ['K0', 'K2', 'K3'])



left.join(right)



left.join(right, 
          how = 'outer')



#OPERATIONS


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
#returns the head of a dataframe
df.head()


#unique values in a column
df["col1"].unique()

#count of unique values
df["col1"].nunique()

#show the count of each unique value
data=df["col1"].value_counts()

print(data)
#selecting data
newdf=df[(df["col1"]>2)&(df["col2"]==444)]

print(newdf)

#applying functions

def func(x):
    return x+1

df["col1"].apply(func)

df['col3'].apply(len)
df['col1'].sum()

#deleting a column
del df["col2"]

#getting column names
df.columns

#getting range index
df.index


#sorting

df.sort_values(by="col1") #use inplace if needed

#find null values (boolean)
df.isnull()



data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

#pivot table

pivot=df.pivot_table(values='D',index=['A','B'],columns=['C'])

print(pivot)



