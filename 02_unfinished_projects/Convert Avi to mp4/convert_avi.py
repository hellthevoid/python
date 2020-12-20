import os
import ffmpy
import ffmpeg-python


avi_file_path="C:\\Users\\sonyx\\Desktop\\Masterarbeit\\Enterprise Dynamics 7 Studio\\Work"
output_name='test'

#ffmpeg -i 'C:\\Users\\sonyx\\Desktop\\Masterarbeit\\Enterprise Dynamics 7 Studio\\Work\\avi1.avi' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'test.mp4'"


for filename in os.listdir(avi_file_path):
    if (filename.endswith(".avi")): #or .avi, .mpeg, whatever.
        os.system("ffmpeg -i {0} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'test.mp4'".format(filename))
    else:
        continue