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
products=['blm2','iep','uhd','lvp']
path="C:\\Users\\sonyx\\Desktop\\Masterarbeit\\ED Models\\"





for product in products:
    df_in=pd.read_csv("{0}t_{1}_in.csv".format(path,product))

    df_in.columns=list(range(len(df_in.columns)))
    #df_out=pd.read_csv("{0}t_{1}_out.csv".format(path,product))
    #df_in.drop(df_in.columns[2:],axis=1,inplace=True)
    
    #print(df_in.head())
    #df_in.drop(df_in.index[:5],axis=0,inplace=True)
    #print(len(df_in.columns))
    #print(df_in.head())
    pdf=PdfPages('{0}.pdf'.format(product))
    #df_in.columns=list(range(10))
    iter_cols=iter(df_in.columns)
    next(iter_cols)
   
    for col in df_in.columns:
        try:
            df_wait=(df_in[next(iter_cols)])-df_in[col]-10
           
            #wait=df_wait.iloc[300:450]

            df_wait=df_wait[df_wait>0.1]
            wait_complete=df_wait
            #print(df_wait.head())
            #print(df_wait.tail())
            if df_wait.empty is False:
                fig=wait_complete.plot(title=col)
                pdf.savefig()
                plt.close()
        except StopIteration:
            pass
    pdf.close()
        
        
        
               # fig=wait_s1_complete.plot(title='Wait time between S1 and S2')
       	#pdf.savefig()
        
   
    
    #df_out.drop(df_out.columns[2:],axis=1,inplace=True)
   # df_out.columns=['s1_out','s2_out']
    
    #df_wait=df_in['s2_in']-df_in['s1_in']-10
   # #df_zau.columns=['zau']
    
    
    
    
df_output=pd.read_csv("{0}{1}.csv".format(path,"output"),header=None)
df_prod=pd.read_csv("{0}{1}.csv".format(path,"produktionsprogramm"),header=None) 
df_output.columns=list(range(len(df_output.columns)))
df_prod.columns=list(range(len(df_prod.columns)))

#print(df_output)
#print(df_prod)


df_check=pd.concat([df_output.iloc[0],df_prod.iloc[0]],axis=1)

print(df_check)
print(df_check.plot.bar())




df_output_m=pd.read_csv("{0}{1}.csv".format(path,"output_m"),header=None)


print(df_)
    #df_zau=df_zau.drop(df_zau.iloc[500:],axis=0,inplace=True)
    
    
    #df_zau=df_zau.drop(axis=0)
    
    #df_in.reset_index()
    #df.set_index('zeit',inplace=True)
    
    
    #(df_wait.iloc[100:])
    #print(df_in.head(5))
    #print(df_out.head(5))
    
    
 
    
    
    
    
    
    
