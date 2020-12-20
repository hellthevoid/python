# -*- coding: iso-8859-1 -*-

from tkinter import *

from pytube import YouTube, Playlist
import concurrent.futures
import tkinter.messagebox
import soundscrape
import subprocess
from tkinterhtml import HtmlFrame
from bs4 import BeautifulSoup
from tk_html_widgets import HTMLLabel



def getAllLinks(playList):
    try:
        allLinks = []
        youtubeLink = 'https://www.youtube.com'
        pl = Playlist(playList)
        [allLinks.append(youtubeLink + linkprefix) for linkprefix in pl.parse_links()] #list comprehension
        return allLinks
    except Exception:
        allLinks=[]
        return allLinks


def open_html():
    with open('youtube_playlist\index1.txt', 'r') as f:

        contents = f.read()

        #soup = BeautifulSoup(contents, 'lxml')
        print(contents)
    return contents

class Application():
    def __init__(self,master):

        contents=open_html()
        master.geometry("1400x800")
        master.title("Youtube/Soundcloud MP3 downloader 9000 - v.0.002")
        
        frame1=Frame(master)
        frame1.grid(row=0)
        
        frame2=Frame(master)
        frame2.grid(row=1)
        
        #tkinter.messagebox.showinfo("Information","If you want to download a whole playlist as MP3's then make sure the link contains the word \"playlist\" in its link.\n e.g. \"https://www.youtube.com/playlist?list=PL3485902CC4FB6C67\"" )
        
        self.button1=Button(frame1,text="Press to download",command=self.buttonclick)
        self.button1.grid(row=1,column=0)
        
        self.entry1=Entry(frame1,width=100)
        self.entry1.grid(row=1,column=1,columnspan=5)

        self.label1=Label(frame1,text="Enter playlist link below:")
        self.label1.grid(row=0,column=1)
        
        self.label2=Label(frame2,text="Status: Unknown")
        self.label2.grid(row=0,column=0,sticky=NW)

        frame3=Frame(master,height=400,width=500)
        frame3.grid(row=2)
        self.lstbx=Listbox(frame3,width=100,height=30)
        self.lstbx.grid(row=1)

        self.credit=Label(frame3,text="Credit: uwekaiMD")
        self.credit.grid(row=0,sticky=E)

        self.info_label=Label(frame3,text="If you want to download a whole playlist as MP3's then make sure the link contains the word \"playlist\" in its link.\n e.g. \"https://www.youtube.com/playlist?list=PL3485902CC4FB6C67\"")
        self.info_label.grid(row=2,sticky=W)
        self.videolist=[]
        
        frame4=Frame(master,height=600,width=1000)
        frame4.grid(row=0,column=6)

       
        self.infotext = HTMLLabel(frame1, html=contents)
        #self.infotext.pack(fill="both", expand=True)
        self.infotext.fit_height()
        self.infotext.grid(row=10,column=6)
          

    def get_entry(self):
        link=self.entry1.get()
        return link

    def fill_list(self,txt):
        self.lstbx.insert(END,txt)
        return txt

    def audio_func(self,song,urls):
            yt=YouTube(song)
            title=yt.title

            idx=urls.index(song)

            #self.videolist.append("Downloading Audio: {0}".format(title))

            print("Downloading Audio: {0}".format(title))

            stream=yt.streams.get_by_itag("140") #audio version 128kb
            stream.download(output_path=".\\youtube",filename_prefix=str(idx).zfill(2)+"_") #zfill->fills zeros to single numbers
            
            self.videolist.append("Audio: {0} - Download finished".format(title))
            print("Audio: {0} - Download finished".format(title))
   
    def buttonclick(self):

        self.label2.config(text="Status: Downloading, please wait!")
        self.label2.update()
        
        if not self.get_entry():
            tkinter.messagebox.showinfo("Information","You didnt enter a playlist link")
            return 0    


        playlistlink=self.get_entry()

        if "soundcloud" in playlistlink:
            process=subprocess.Popen("soundscrape {}".format(playlistlink),stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output)
            self.videolist.append("Audio: {0} - Download finished".format(playlistlink))
        else:
            urls=getAllLinks(playlistlink)
            
            if not urls:
                urls.append(playlistlink)

            count_songs=len(urls)

            tkinter.messagebox.showinfo("Estimated time","Your playlist contains {0} audio files, this may take a while. May vary due to your internet connection and length of the audios. I recommend letting the program run in the background. The downloaded files will be in the folder named youtube (next to the .exe)".format(count_songs))

            #Multi-threading - downloading multiple Audios at once
            executor = concurrent.futures.ThreadPoolExecutor(5)
            futures = [executor.submit(self.audio_func,song,urls) for song in urls] #list comprehension
            concurrent.futures.wait(futures)

        [self.fill_list(item) for item in self.videolist]
            
        
        self.lstbx.update()
        self.label2.config(text="Status: Finished!")
        tkinter.messagebox.showinfo("Information","All the downloads are finished, you may close the program")




root=Tk()

app=Application(root)

root.mainloop()

