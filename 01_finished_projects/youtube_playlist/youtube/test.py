
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


song='https://www.youtube.com/watch?v=amwQytRNvEw&ab_channel=juancarloscadavidsanchez'
#pl=getAllLinks(playlistlink)

#count_songs=len(pl.video_urls)


#Multi-threading - downloading multiple Audios at once
#executor = concurrent.futures.ThreadPoolExecutor(3)
#futures = [executor.submit(self.audio_func,song,pl.videos) for song in pl.videos] #list comprehension
#concurrent.futures.wait(futures)
song=YouTube(song)
idx=1

#=pl.videos
#for song in videos:
print(song.streams.filter(only_audio=True).all())
stream=song.streams.get_by_itag("140") #audio version 128kb
stream.download(output_path=".\\youtube",filename_prefix=str(idx+1).zfill(2)+"_") 