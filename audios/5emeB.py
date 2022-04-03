"""
Projet STARCK 
"""

"""
A : OK
Text to MP3
Install Python
Install gTTS
$ sudo apt install python3-gtts
$ gtts-cli --help | more
https://gtts.readthedocs.io/en/latest/cli.html
$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3
BUG:
s='gtts-cli "'+CurrentLine+'" --lang fr --output A05'+f+".mp3"
$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3
usage: gtts-cli [-h] [-f FILE] [-o DESTINATION] [-l LANG] [--slow] [--debug]
                [text]
gtts-cli: error: unrecognized arguments: --output cestlavie.mp3
SOLUTION:
gtts-cli -o cestlavie.mp3 -l fr "c'est la vie"  
"""

"""
B : Texte

OK: 


NEW : 
$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3

BUG (old version) : 
    s="gtts-cli -o A05"+f+".mp3 -l fr "+'"'+CurrentLine+'"'
"""

import os

filecsv = open('Speechs.csv', 'r')
Lines = filecsv.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    f = "%02d" % (count)
    CurrentLine=line.strip()
    print(f)
    print(CurrentLine)
    s="gtts-cli "+CurrentLine+" --lang fr --output B05"+f+".mp3"
    print(s)
    os.system(s)

"""
Under DOS : 
>copy /b A*.mp3 + B*.mp3 C*.mp3
OK

---

BUG :
https://github.com/anars/blank-audio/blob/master/1-second-of-silence.mp3

>copy /b 1s.mp3 + 1s.mp3 2s.mp3
OK

>copy /b A*.mp3 + 1s.mp3 C*.mp3
KO
>copy /b 1s.mp3 + C*.mp3 D*.mp3
KO

"""

"""
BUG : 
Error: 429 (Too Many Requests) from TTS API. Probable cause: Unknown
WORKAROUND :
Mobile Access Point
"""
