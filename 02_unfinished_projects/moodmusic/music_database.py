from os import read, replace
import pandas as pd
import numpy as np
import csv
import os
import sys
from  numpy.random import randn
import random
import shutil
from datetime import date, datetime
import os, winshell
from win32com.client import Dispatch
import re
import rym_tags

today = str(datetime.now())
today=today.replace(':','-')

#create a shortcut to an acntual album
def create_shortcut(dest,src_path,complete_album,tag):
    
    dest = dest+str(tag) # path to where you want to put the .lnk
    if not os.path.exists(dest):
        os.makedirs(dest)

        #convention
       # : -> _
       # ? -> __
       # / -> ___
       # ! -> ____
       # ... -> _____

    new_complete_folder_album= replace_forbidden_symbols(complete_album)

    shortcut_path = os.path.join(dest, '{0}.lnk'.format(new_complete_folder_album))

    shell = Dispatch('WScript.Shell')
    try:
        shortcut = shell.CreateShortCut(shortcut_path)
    #src_path=Path(src_path)

        shortcut.Targetpath = src_path
        shortcut.save()
    except:
        pass
        print("Couldnt create shortcut:{0}".format(shortcut_path))

##to do##
def create_all_shortcuts():

    df=read_db('music_database.csv')
    
    #dest="C:\\Users\\sonyx\\Desktop\\moodmusic_phone\\"

    dest='D:\\Musik\\moodmusic\\'
    #src_path_base='Computer\\sonyx_phone\\SD card\\Soundperlen\\'
    src_path_base='D:\\Musik\\Soundperlen\\'
    
    for index in df.index.values.tolist():
        artist=df.iloc[index]['artist']
        album=df.iloc[index]['album']
        genre=df.iloc[index]['genre']
        complete_album=df.iloc[index]['complete_album']
        tags=df.iloc[index,3:8].tolist()

        src_path = "{0}{1}\\{2}\\{3}".format(src_path_base, genre,artist, complete_album) 
        src_path=replace_forbidden_symbols(src_path)
        src_path=src_path.replace("D_","D:")
        [create_shortcut(dest,src_path,complete_album,tag) for tag in tags]

def pop_db(df, artist,album):
    ##TO DO -> Remove shortcut as well
    data=df[(df['artist']==artist & df['album']==album)]
    print(data)
    df.drop(data.index,inplace=True)
    return df

def dataframe_difference(df1, df2, which=None):
    #which='left_only'  and which='right_only' and which='both'
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2, indicator=True, how='outer')

    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    #diff_df.to_csv('data_diff.csv')
    return diff_df

#look through db if all albums are still in the right place
def compare_db():
    #which='left_only'  and which='right_only' and which='both'


    #look through db if all albums are still in the right pla
    #https://stackoverflow.com/questions/20225110/comparing-two-dataframes-and-getting-the-differences

    #see what the new folder structure looks like
    new_df=init_db('music_database_copy.csv')
    #print(new_df)
    t_new_df=new_df.iloc[:,0:9]
    t_new_df.drop('tag1',axis=1,inplace=True)
    t_new_df.drop('tag2',axis=1,inplace=True)
    t_new_df.drop('tag3',axis=1,inplace=True)
    t_new_df.drop('tag4',axis=1,inplace=True)
    t_new_df.drop('tag5',axis=1,inplace=True)

    t_new_df=translate_forbidden_symbols(t_new_df)

    #print(t_new_df)
    #get the current database structure
    df=read_db('music_database.csv')

    t_df=df.iloc[:,0:9]
    t_df.drop('tag1',axis=1,inplace=True)
    t_df.drop('tag2',axis=1,inplace=True)
    t_df.drop('tag3',axis=1,inplace=True)
    t_df.drop('tag4',axis=1,inplace=True)
    t_df.drop('tag5',axis=1,inplace=True)

    #get difference
    delta_df=dataframe_difference(t_new_df,t_df)
    right_only=delta_df[delta_df['_merge']=='right_only'] #new albums
    left_only=delta_df[delta_df['_merge']=='left_only'] #old albums

    #remove old albums
    selection=right_only.complete_album.tolist()
    tt_df=df[~pd.DataFrame(df['complete_album'].tolist()).isin(selection).any(1)] #~ means negative 
    df=tt_df

    print(left_only)
    ####add new albums####
    frames=[df,left_only]

    df=pd.concat(frames,ignore_index=True)
    cols=['artist','album','genre','tag1','tag2','tag3',
        'tag4','tag5','complete_album','rym_genre1','rym_genre2','rym_genre3','year','rating','search_result1','search_result2','search_result3']

    #rearrange cols
    df=df[cols]

    return df

#read the csv file into a dataframe
def read_db(fcsv):
    df=pd.read_csv(fcsv,encoding='UTF-8')

    if 'Unnamed: 0' in df:
        df.drop('Unnamed: 0',axis=1,inplace=True)
    df=df.astype('object',copy=False)
    return df

#change an album row manually
def change_manually(df):
    while index!=0:
        index=input('which index do you want to change? Enter 0 if you want to cancel')
        df.at[index,'tag1']=input('Please enter Tag1: ')
        df.at[index,'tag2']=input('Please enter Tag2: ')
        df.at[index,'tag3']=input('Please enter Tag3: ')
        df.at[index,'tag4']=input('Please enter Tag4: ')
        df.at[index,'tag5']=input('Please enter Tag5: ')
        df.at[index,'rym_genre1']=input('Please enter Genre1: ')
        df.at[index,'rym_genre2']=input('Please enter Genre2: ')
        df.at[index,'rym_genre3']=input('Please enter Genre3: ')
        df.at[index,'year']=input('Please enter Year: ')
        df.at[index,'rating']=input('Please enter Rating: ')

    return df

def translate_forbidden_symbols(df):
    ##############TO DO################
    #convention
       # : -> _
       # ? -> __
       # / -> ___
       # ! -> ____
       # ... -> _____
    
    #df.replace(to_replace=r'_4',value=r"____",inplace=True,regex=True)
    #df.replace(to_replace=r'_5',value=r"_____",inplace=True,regex=True)

    df.replace(value=r'\.\.\.',to_replace=r"_____",inplace=True,regex=True)
    df.replace(value=r'!',to_replace=r"____",inplace=True,regex=True)
    df.replace(value=r'/',to_replace=r"___",inplace=True,regex=True)
    df.replace(value="?",to_replace=r"__",inplace=True,regex=True)
    #df=df['album'].replace(value=r':',to_replace=r'_',regex=True)

    df.replace(to_replace=r'_',value=r':',inplace=True,regex=True)
    #df.replace(to_replace=r'Elliott',value=r'aaa',inplace=True,regex=True)
    #print(df[df['artist'].str.contains('_')])
    #print(df[df['album'].str.contains('_')])

    df_new=df

    return df_new

def replace_forbidden_symbols(value):
        #convention
       # : -> _
       # ? -> __
       # / -> ___
       # ! -> ____
       # ... -> _____


    value=value.replace(":","_")
    value=value.replace("?","__")
    value=value.replace("/","___")
    value=value.replace("!","____")
    value=value.replace("...","_____")

    return value

def reset_search_result(df,index):
    df.at[index,'tag1']=np.nan
    df.at[index,'tag2']=np.nan
    df.at[index,'tag3']=np.nan
    df.at[index,'tag4']=np.nan
    df.at[index,'tag5']=np.nan
    df.at[index,'rym_genre1']=np.nan
    df.at[index,'rym_genre2']=np.nan
    df.at[index,'rym_genre3']=np.nan
    df.at[index,'year']=np.nan
    df.at[index,'rating']=np.nan
    df.at[index,'search_result1']=np.nan
    df.at[index,'search_result2']=np.nan
    df.at[index,'search_result3']=np.nan

#################INCOMPLETE###############
#decide which search result is correct for a bad search result and change directory accordingly
def decision_time(df):
    #TEST
    src_path_base='D:\\Musik\\Soundperlen\\'
    criteria1=(df['tag2']=='bad search result')
    criteria2=df['search_result1']

    data=df[(criteria1&criteria2)]
    print(len(data))

    for index,row in data.iterrows():
        artist=df.iloc[index]['artist']
        album=df.iloc[index]['album']
        genre=df.iloc[index]['genre']
        complete_album=df.iloc[index]['complete_album']
        search_result1=eval(df.iloc[index]['search_result1'])#convert to real tuple
        search_result2=eval(df.iloc[index]['search_result2'])
        search_result3=eval(df.iloc[index]['search_result3'])

        print(artist)
        print(album)
        print(df.iloc[index]['search_result1'])
        print(df.iloc[index]['search_result2'])
        print(df.iloc[index]['search_result3'])

        try:
            decision=int(input('Please Choose 0-1-2-3:'))
        except:
            decision=0
        

        if decision==1:
            new_artist=search_result1[0]
            new_album=search_result1[1]
        elif decision==2:
            new_artist=search_result2[0]
            new_album=search_result2[1]
        elif decision==3:
            new_artist=search_result3[0]
            new_album=search_result3[1]
        else:
            ###to do###
            x=input('Do you want to reset the index?(y/n)')
            if x=='y':
                reset_search_result(df,index)
            else:
                print('please change manually')

            continue
        

        new_complete_album=new_artist+' - '+new_album
        


        #empty row

        for col in range(0,len(df.iloc[index])):
            df.iat[index,col]=np.nan


        #set row with new inital values
        df.at[index,'complete_album']=new_complete_album
        df.at[index,'artist']=new_artist
        df.at[index,'album']=new_album
        df.at[index,'genre']=genre

        print(df.iloc[index])
        #find all other albums with the same artist
        df_same_artist=df[df['artist']==artist]

        print(df_same_artist)

        ######TO DO#################
        ##if artist has to change also change:
        # -artist directory name of every other album -> wrong no need to do it
        # - artist in database -> find all entrys with same artist name and change -> list them and ask for change
        # - already created shortcuts
        # -##################

        #change artist path if necessary
        src_path = "{0}{1}\\{2}".format(src_path_base, genre,artist)

        new_folder_artist=replace_forbidden_symbols(new_artist)

        target_path="{0}{1}\\{2}".format(src_path_base, genre,new_folder_artist)
        if artist!=new_artist:
            try:
                os.rename(src_path,target_path)
            except Exception as e:
                print(e)
        
        
        #change album directory
        src_path = "{0}{1}\\{2}\\{3}".format(src_path_base, genre,new_artist, complete_album)

        new_complete_folder_album=replace_forbidden_symbols(new_complete_album)

        target_path="{0}{1}\\{2}\\{3}".format(src_path_base, genre,new_artist, new_complete_folder_album)
        if complete_album!=new_complete_album:
            try:
                os.rename(src_path,target_path)
            except Exception as e:
                print(e)


        if not df_same_artist.empty and new_artist!=artist:
            for index, row in df_same_artist.iterrows():
                    print(row)
                    inp=input('Should this album also be changed? (y/n)')
                    if inp=='y':
                        df.at[index,'artist']=new_artist
                        #df.at[index,'complete_album']=new_artist+' - '+df.loc[index,'album']
                        print(df.iloc[index])

                        
                        album=df.iloc[index]['album']
                        genre=df.iloc[index]['genre']
                        complete_album=df.iloc[index]['complete_album']
                        new_complete_album=new_artist + ' - '+album
                        
                        #change album directory
                        src_path = "{0}{1}\\{2}\\{3}".format(src_path_base, genre,new_artist, complete_album)

                        new_complete_folder_album=replace_forbidden_symbols(new_complete_album)

                        target_path="{0}{1}\\{2}\\{3}".format(src_path_base, genre,new_artist, new_complete_folder_album)

                        df.at[index,'complete_album']=new_complete_album

                        if complete_album!=new_complete_album:
                            try:
                                os.rename(src_path,target_path)
                            except Exception as e:
                                print(e)
                        



        save_df('music_database.csv',df)

    return df

def save_df(fname,df):
    #backup old database
    shutil.copyfile(fname,'C:\\Users\\sonyx\\python\\04_backup_music_database\\{}_music_database.csv'.format(today))
    
    #save new data
    f = open(fname, "w+",encoding='UTF-8') #clear first file?
    f.close()
    df.to_csv(fname,encoding='UTF-8')

#write the attributes to an album row (from rym)
def write_attributes(df,row,tags,genres,year,rating,sr1,sr2,sr3):
    df=df.astype('object',copy=False)

    df.iat[row,3]=tags[0]
    df.iat[row,4]=tags[1]
    df.iat[row,5]=tags[2]
    df.iat[row,6]=tags[3]
    df.iat[row,7]=tags[4]
    df.iat[row,9]=genres[0]
    df.iat[row,10]=genres[1]
    df.iat[row,11]=genres[2]
    df.iat[row,12]=year
    df.iat[row,13]=rating
    df.iat[row,14]=sr1
    df.iat[row,15]=sr2
    df.iat[row,16]=sr3

    print(df.iloc[row,:])

    return df

#get a album row that is not complete yet (no tags or bad search result)
def get_rand(df):
    
    #no tags yet
    criteria1=pd.isnull(df['tag2'])

    #bad search result and no search result yet
    criteria2=(df['tag2']=='bad search result') & pd.isnull(df['search_result1'])

    data1=df[(criteria1|criteria2)]
    
    print(data1)

    if len(data1.index)==0:
        print('its all done!')
        exit()
    
    rand_choice=random.randint(0,len(data1.index)-1)
    rand_num=data1.iloc[rand_choice]
    
    print(rand_num)

    artist=rand_num['artist']
    album=rand_num['album']
    genre=rand_num['genre']
    complete_album=rand_num['complete_album']
    row=rand_num.name

    return artist, album,genre,row,complete_album


#create an initial empty dataframe
def write_init_db(df,artist,album,genre,album_folder):

    my_list=[artist,album,genre,'','','','','',album_folder,'','','','','','','','']
    #sers=pd.Series(data=my_list,)
    df.loc[len(df)]=my_list
    #df.append(sers,ignore_index=True)
    return df

#iniate a database 
def init_db(fcsv):
    f = open(fcsv, "w+",encoding='UTF-8') #clear first file?
    f.close()
    mtx=np.random.rand(0,17)
    cols=['artist','album','genre','tag1','tag2','tag3',
    'tag4','tag5','complete_album','rym_genre1','rym_genre2','rym_genre3','year','rating','search_result1','search_result2','search_result3']
    df=pd.DataFrame(mtx,columns=cols)
    df=df.astype('object',copy=False) #convert df to string

    #print(df.dtypes)
    df.to_csv(fcsv,encoding='UTF-8') #fill file with columns so empty column can be removed?

    df=read_db(fcsv) # remove empty column?

    src_path_base='D:\\Musik\\Soundperlen\\'

    '''
    ##############check##############
    

    pattern=re.compile(r"([a-zA-Z0-9) (.]*[a-zA-Z0-9)(.]-[a-zA-Z0-9)(.][a-zA-Z0-9) (.]*)")
    matches=[]
    for folderNames,subfolders,fNames in os.walk(src_path_base):
        for folder in subfolders:
            matches=pattern.finditer(folder)
            for match in matches:
                print(folder)
            try:
                matches.clear()
            except:
                pass
    #############check##############
    '''
    #random album anfragen, vorher in liste speichern
    for folderNames,subfolders,fNames in os.walk(src_path_base):
        
        for folder in subfolders:

            matches=re.search(r"(CD[0-9])",folder) #get folders that are CD folders and ignores them
            #if matches:
            #    print(matches.string)
            
            if " - " in folder and not matches: #characterizes an album
                
                #set attributes
                genre=folderNames.split("\\")[-2]
                artist=folder.split(" - ")[0]
                album=folder.split(' - ')[-1]

                #remove eg [FLAC] characters from album
                album_match=re.search(r'(\[.*\])',album)
                if album_match:
                    album_match=album_match.group(0)
                    album=album.replace(album_match,'')
                    #print(album)
                
                #remove eg (***) characters from album
                album_match=re.search(r'([(].+[)])',album)
                if album_match:
                    album_match=album_match.group(0)
                    #print(album)
                    #print (album_match)
                    album=album.replace(album_match,'')
                    #print(album)
                

                #match anything with 3 "-"
                album_match=re.search(r'(.+ - .+ - .+ - .+)',folder)
                if album_match:
                    album_match=album_match.group(0)
                    
                    print(folder)
                    #print (album_match)
                    #album=album.replace(album_match,'')
                    #print(album)
                    path=os.path.join(folderNames,folder)
                    path = os.path.realpath(path)
                    os.startfile(path) #open the folders in explorer!
                '''
                album_match=re.search(r'(.* -.*!(\d\d\d\d).*- .*)',folder)
                if album_match:
                    album_match=album_match.group(0)
                    
                    print(folder)
                    #print (album_match)
                    #album=album.replace(album_match,'')
                    #print(album)
                    path=os.path.join(folderNames,folder)
                    path = os.path.realpath(path)
                    os.startfile(path) #open the folders in explorer!
                '''

                df=write_init_db(df,artist,album,genre,folder) # write attributes to database

    df.to_csv(fcsv,encoding='UTF-8')
    return df

if __name__ == '__main__':
    #shutil.copyfile('music_database.csv','C:\\Users\\sonyx\\python\\04_backup_music_database\\{}_music_database.csv'.format(today))
    #init_db()
    df=read_db('music_database.csv')

    #df['search_result1']=np.nan
    #df['search_result2']=np.nan
    #df['search_result3']=np.nan
    #df=get_bad_search_results(df)
    #print(df)
    #df.to_csv('music_database.csv',encoding='UTF-8') #fill file with columns so empty column can be removed?

    pass