

import soundscrape
import subprocess

link=input("Please enter soundcloud link")


process=subprocess.Popen("soundscrape {}".format(link),stdout=subprocess.PIPE)
output, error = process.communicate()
#print(output)


