# -*- coding: iso-8859-1 -*-

#import concurrent.futures
import os
import subprocess
import tkinter.messagebox
from tkinter import *
#from tkinter.ttk import *
from datetime import datetime
import re

import soundscrape
from pytube import Playlist, YouTube
from tk_html_widgets import HTMLLabel


def getAllLinks(playList):

    allLinks = []
    # this fixes the empty playlist.videos list
    pl = Playlist(playList)
    pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print(len(pl.video_urls))

    for url in pl.video_urls:
        print(url)

    
    return pl

def open_html():
    try:
        with open(os.path.join(os.path.dirname(__file__), "main.txt"), "r") as f:

            contents = f.read()
    except:
        contents=""

    return contents

class Application():
    def __init__(self,master):

        contents=open_html()
        master.geometry("1100x600")
        master.title("Youtube/Soundcloud MP3 downloader 9000 - v.0.002")
        #p1 = PhotoImage(file = 'C:\\Users\\sonyx\\python\\02_unfinished_projects\\youtube_playlist\\info.png')
 
        # Setting icon of master window
        #master.iconphoto(False, p1)
        frame0=Frame(master)
        frame0.grid(row=0,column=0,padx=0,pady=10)

        frame1=Frame(master)
        frame1.grid(row=1,column=0)

        frame2=Frame(master)
        frame2.grid(row=0,column=1)

        now=datetime.now()
        year=int(now.year)

        if year>2022:
            tkinter.messagebox.showerror(message="Sorry this software has expired, please write to fluss.acid@gmail.com for a newer better version!")
            exit()

        #Download Button
        self.button1=Button(frame0,text="Press to download",command=self.buttonclick,bg='#9BEAD3')
        self.button1.grid(row=0,column=0,pady=5,padx=10,sticky=W)
        
        #Adresszeile
        self.entry1=Entry(frame0,width=100)
        self.entry1.grid(row=1,column=0,padx=10,pady=10,sticky=W)#',columnspan=5)

        #Enter playlist label
        self.label1=Label(frame0,text="Enter playlist link below:")
        self.label1.grid(row=0,column=0)
        
        #Status label
        self.label2=Label(frame0,text="Status: Unknown")
        self.label2.grid(row=2,column=0,padx=20,sticky=E)

        ##Infotext       
        self.infotext = HTMLLabel(frame0, html=contents)
        #self.infotext.pack(fill="both", expand=True)
        #self.infotext.fit_height()
        self.infotext.grid(row=1,rowspan=4,column=1,sticky=N)

        #Listbox
        self.lstbx=Listbox(frame0,width=79,height=20)
        self.lstbx.grid(row=3,column=0,pady=10)

        #Credit Label
        self.credit=Label(frame0,text="Credit: uwekaiMD")
        self.credit.grid(row=2,column=0,sticky=W,padx=10)

        self.info_label=Label(frame0,text="If you want to download a whole youtube playlist as MP3's \n then make sure the link contains the word \"playlist\" in its link.\n e.g. \"https://www.youtube.com/playlist?list=PL3485902CC4FB6C67\"")
        self.info_label.grid(row=4,pady=10)
        self.videolist=[]

        s=("The Youtube music gets saved in the 'youtube' folder \n and the Soundcloud music get saved in the 'soundcloud' folder.\n"
        "Please be patient as the program will freeze during the download.\n\n"
        "If you would like to support my work feel free to buy me a beer.\n"
        "Or write a mail for bugs and updates to: fluss.acid@gmail.com")

        self.info_label2=Label(frame0,text=s)
        self.info_label2.grid(row=4,column=1,pady=10,sticky=W)


    def get_entry(self):
        link=self.entry1.get()
        return link
    
    
    def refresh(self):
        self.root.update()
        self.root.after(1000,self.refresh)

    def fill_list(self,txt):
        self.lstbx.insert(END,txt)
        return txt

    def audio_func(self,song,idx):
            #yt=YouTube(song)
            title=song.title
            print(title)
            try:
                #idx=urls.index(song)

                #self.videolist.append("Downloading Audio: {0}".format(title))

                #print("Downloading Audio: {0}".format(title))
               # print(song.streams.filter(only_audio=True).all())
                stream=song.streams.get_by_itag("140") #audio version 128kb
                stream.download(output_path=".\\youtube",filename_prefix=str(idx+1).zfill(2)+"_") #zfill->fills zeros to single numbers
                
                txt=("Audio: {0} - Download finished".format(title))
                self.lstbx.insert(END,txt)
                #self.refresh
                #print("Audio: {0} - Download finished".format(title))

            except Exception as e:
                print("Error is: "  + str(e))
                txt=("Audio: {0} - Download FAILED".format(title))
                self.lstbx.insert(END,txt)
                print("Audio: {0} - Download FAILED".format(title))
   
    def buttonclick(self):

        self.label2.config(text="Status: Downloading, please wait!")
        self.label2.update()
        
        if not self.get_entry():
            tkinter.messagebox.showinfo("Information","You didnt enter a playlist link")
            return 0    


        playlistlink=self.get_entry()
        #test if encoding is necessary!!
        if "soundcloud" in playlistlink:
            subprocess.run("soundscrape -p {0} {1}".format(soundcloud_dir,playlistlink))
            #output, error = process.communicate()
            #lines = output.decode("iso-8859-1").splitlines()
            #print(lines)
            txt=("Audio: {0} - Download finished".format(playlistlink))
            self.lstbx.insert(END,txt)
        else:
            
            try:
                pl=getAllLinks(playlistlink)
                count_songs=len(pl.video_urls)
                idx=0
                tkinter.messagebox.showinfo("Estimated time","Your playlist contains {0} audio files, this may take a while. May vary due to your internet connection and length of the audios. I recommend letting the program run in the background. The downloaded files will be in the folder named youtube (next to the .exe)".format(count_songs))
                for song in pl.videos:
                    self.audio_func(song,idx)
                    idx=idx+1
                
            except: #just a single song
                count_songs=1
                tkinter.messagebox.showinfo("Estimated time","Your playlist contains {0} audio files, this may take a while. May vary due to your internet connection and length of the audios. I recommend letting the program run in the background. The downloaded files will be in the folder named youtube (next to the .exe)".format(count_songs))
                pl=playlistlink
                
                song=YouTube(pl)
                self.audio_func(song,1)            

            #Multi-threading - downloading multiple Audios at once
            
            #executor = concurrent.futures.ThreadPoolExecutor(3)
            #futures = [executor.submit(self.audio_func,song,idx,pl.videos) for idx,song in enumerate(pl.videos)] #list comprehension
            #concurrent.futures.wait(futures)
            

            
        
           
        
        self.lstbx.update()
        self.label2.config(text="Status: Finished!")
        tkinter.messagebox.showinfo("Information","All the downloads are finished, you may close the program")


#Main




cwd=os.path.dirname(__file__)
soundcloud_dir=os.path.join(cwd, "soundcloud")
if not os.path.exists(soundcloud_dir):
    os.mkdir(os.path.join(cwd, "soundcloud"))
if not os.path.exists(os.path.join(cwd, "youtube")):
    os.mkdir(os.path.join(cwd, "youtube"))

root=Tk()

app=Application(root)

root.mainloop()

