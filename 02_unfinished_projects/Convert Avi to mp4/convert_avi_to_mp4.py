# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:39:57 2019

@author: sonyx
"""

import os


avi_file_path="C:\\Users\\sonyx\\Desktop\\Masterarbeit\\Enterprise Dynamics 7 Studio\\Work\\avi1.avi"
output_name='test'
def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    return True


convert_avi_to_mp4(avi_file_path,output_name)


