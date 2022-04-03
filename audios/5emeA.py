"""
Projet STARCK 
"""

"""
Text to MP3
Install Python
Install gTTS
$ sudo apt install python3-gtts
$ gtts-cli --help | more
https://gtts.readthedocs.io/en/latest/cli.html
$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3

SOLUTION:
s='gtts-cli "'+CurrentLine+'" --lang fr --output A05'+f+".mp3"
$ sudo apt install python3-pip
$ pip install gTTS
$ gtts-cli
$ gtts-cli --help
$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3

BUG (Old Version):
OK : Also Working ...
    s="gtts-cli -o A05"+f+".mp3 -l fr "+'"'+CurrentLine+'"'
usage: gtts-cli [-h] [-f FILE] [-o DESTINATION] [-l LANG] [--slow] [--debug]
                [text]
gtts-cli: error: unrecognized arguments: --output cestlavie.mp3
gtts-cli -o cestlavie.mp3 -l fr "c'est la vie"  
"""

import os

filecsv = open('Titles.csv', 'r')
Lines = filecsv.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    f = "%02d" % (count)
    CurrentLine=line.strip()
    print(f)
    print(CurrentLine)
    s='gtts-cli "'+CurrentLine+'" --lang fr --output A05'+f+".mp3"
    print(s)
    os.system(s)    

