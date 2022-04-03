"""
Projet STARCK 
"""

"""
STEP 1 : PDF to SVGs
Install Python
Install Inkscape (Open Source) https://alternativeto.net/software/inkscape/about/
https://inkscape.org/release/inkscape-1.0.2/
cd C:\"Program Files"\Inkscape\bin\
+ CHANGE CODE : 
    s='inkscape --export-filename=C:\\Tmp\\05'+file+'.svg --pdf-page='+page+' C:\\Tmp\\5emeArr.pdf'
C:\"Program Files"\Inkscape\bin\python C:\Tmp\5eme.py
"""

"""
STEP 2 : SVGs to PNGs
Install ImageMagick (Open Source) https://alternativeto.net/software/imagemagick/about/
https://imagemagick.org/script/download.php
cd C:\"Program Files"\ImageMagick-7.0.11-Q16-HDRI>
+ CHANGE CODE :
    s="magick C:\\Tmp\\05"+file+".svg C:\\Tmp\\05"+file+".png"
python C:\Tmp\5eme.py
"""

"""
ToDo : 
STEP 3 : PNGs to TXTs
Install tesseract (Open Source) https://alternativeto.net/software/tesseract/about/
https://github.com/tesseract-ocr/tesseract
On Linux (or VirtualBox)
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev
$ tesseract --version
tesseract 4.1.1
TBC...

"""

import os

for i in range(61): """ Number of pages = 61 """
    print(i+1)
    page = "%d" % (i+1) """ page = 1 """
    file = "%02d" % (i+1) """ file = 01 """
    print(page)
    print(file)
    s="magick C:\\Tmp\\05"+file+".svg C:\\Tmp\\05"+file+".png"
    print(s)
    os.system(s)



"""
N.B. :
DOESN'T WORK 
os.system("cd C:\"Program Files"\Inkscape\bin\")
doesn't work, you have to launch programs from thier folders
"""
"""
DOESN'T WORK ! 
s = 'C:\\"Program Files"\\Inkscape\\bin\\inkscape --export-filename=C:\\Tmp\\05'+file+'.svg --pdf-page='+page+' C:\\Tmp\\5emeArr.pdf'
"""
"""
We didn't use .BAT files (not portable on Linux)
    os.system("C:\Windows\System32\cmd.exe /c z:\Scripts\myscript.bat")
"""
