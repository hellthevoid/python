# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:10:03 2019

@author: sonyx
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from matplotlib.backends.backend_pdf import PdfPages


#****************************************
####access each column index to create graphic####
#if 0 or minus stop
#iterator=next
#***********************************************
products=['BLM2','IEP','UHD','LVP']
path="C:\\Users\\sonyx\\Desktop\\Masterarbeit\\ED Models\\"

plt.style.use("seaborn")

df_last_time=pd.DataFrame(np.random.randint(5,size=(4,1)))

print(df_last_time.dtypes)

for idx,product in enumerate(products):
    df_in=pd.read_csv("{0}t_{1}_in.csv".format(path,product),header=None)

    #df_in.columns=list(range(len(df_in.columns)))
    #df_out=pd.read_csv("{0}t_{1}_out.csv".format(path,product))
    #df_in.drop(df_in.columns[2:],axis=1,inplace=True)
    
    print(df_in.head())
    #df_in.drop(df_in.index[:5],axis=0,inplace=True)
    #print(len(df_in.columns))
    #print(df_in.head())
    pdf=PdfPages('{0}.pdf'.format(product))
    #df_in.columns=list(range(10))
    
    df_in=df_in.loc[:,(df_in!=0).any(axis=0)] #drop all columns with only 0s
    df_in=df_in.loc[(df_in!=0).any(axis=1),:] #drop all rows with only 0s
    
    
    print(df_in)
    #make an iterator out of the column names and go to next one with next()
    iter_cols=iter(df_in.columns)
    next(iter_cols)
    
    for col in df_in.columns:
        try:
            df_wait=(df_in[next(iter_cols)])-df_in[col]-10
           
            #wait=df_wait.iloc[300:450]

            df_wait=df_wait[df_wait>0.1]
            #print(df_wait.head())
            #print(df_wait.tail())
            if df_wait.empty is False:
                fig=df_wait.plot(title='Wartezeit vor Maschine{0}'.format(col+2))
                pdf.savefig()
                plt.close()
        except StopIteration:
            pass
    pdf.close()
    
    
    
    
    df_last_time.iat[idx,0]=df_in.iloc[-1,0]
    df_last_time.columns=['last element time']
    print(df_last_time)
    
    
    
    
    #print(df_in)
    df_dlz=df_in.iloc[:,[0,-1]].copy()
    df_dlz['DLZ']=df_dlz.iloc[:,1]-df_dlz.iloc[:,0]
    df_dlz=df_dlz.loc[(df_dlz>0).any(axis=1),['DLZ']]
    df_dlz=df_dlz.loc[(df_dlz>0).any(axis=1),['DLZ']]
    #print(df_dlz)
    
    df_dlz.plot.line(title=product)
    plt.show()
    plt.close()



#df_dlz.plot.bar()
###Output Vergleich###    

df_output=pd.read_csv("{0}{1}.csv".format(path,"output"),header=None)
df_prod=pd.read_csv("{0}{1}.csv".format(path,"produktionsprogramm"),header=None) 
#df_output.columns=list(range(len(df_output.columns)))
#df_prod.columns=list(range(len(df_prod.columns)))

print(df_output)
print(df_prod)


df_check=pd.concat([df_output.iloc[0],df_prod.iloc[0]],axis=1)
df_check.index=products
df_check.columns=["Ist-Schicht-Stückzahlen",'Soll-Schicht-Stückzahlen']
df_check.plot.bar(title='Stückzahlerfüllungsgrad',rot=0)
plt.show()
plt.close()

#ist falsch -> 28000 zeit beim letzten atom df_in letztes atom+10


#df_check.insert(len(df_check.columns),'Taktzeit',[0,0,0,0],True)
#df_check.index.name='prodname'

print(df_check)



df_check['Taktzeit']=df_last_time["last element time"]/df_check["Ist-Schicht-Stückzahlen"]



df_check['Taktzeit'].plot.bar(title='Taktzeit',rot=0)
print(df_check)




df_output_m=pd.read_csv("{0}{1}.csv".format(path,"output_m"),header=None)

df_output_m.drop(df_in.columns[0],axis=1,inplace=True)

df_output_m["Auslastung"]=df_output_m[2]*10*100/28000


df_output_m.drop(df_in.columns[2],axis=1,inplace=True)

df_output_m.set_index(df_output_m[1],inplace=True)

df_output_m.drop(df_in.columns[1],axis=1,inplace=True)

df_output_m.sort_values(by=['Auslastung'],inplace=True,ascending=False)

print(df_output_m)


df_output_m.plot.bar(title='Auslastung',rot=45)

    


    

    
    
    
