import os

"""
Q05xx.png
.png : 792 x 1120
Cut at Width = 581
=> 581x1120
"""

for i in range(61):
    print(i+1)
    page = "%d" % (i+1)
    file = "%02d" % (i+1)
    print(page)
    print(file)
    s="magick C:\\Tmp\\T05"+file+'.png -fill "rgb(255,255,255)" -draw "rectangle 425,900 581,1120" -draw "rectangle 535,550 581,1120" -draw "rectangle 522,625 581,1120" C:\\Tmp\\Q05'+file+".png"
    print(s)
    os.system(s)


"""
OK / DONE !

1. InkScape : PDF -> SVG
cd C:\"Program Files"\Inkscape\bin\
    s='inkscape --export-filename=C:\\Tmp\\05'+file+'.svg --pdf-page='+page+' C:\\Tmp\\5emeArr.pdf'

2. ImageMagick : SVG -> PNG
cd C:\"Program Files"\ImageMagick-7.0.11-Q16-HDRI
    s="magick C:\\Tmp\\05"+file+".svg C:\\Tmp\\05"+file+".png"

3. ImageMagick : PNG / Crop
cd C:\"Program Files"\ImageMagick-7.0.11-Q16-HDRI
    s="magick C:\\Tmp\\05"+file+".png -crop 581x1120+0+0 C:\\Tmp\\T05"+file+".png"
=> 581x1120

4. ImageMagick : PNG / Draw White
cd C:\"Program Files"\ImageMagick-7.0.11-Q16-HDRI
    s="magick C:\\Tmp\\T05"+file+".png -fill "rgb(0,0,0)" -draw "rectangle 425,900 581,1120" -draw "rectangle 535,550 581,1120" C:\\Tmp\\Q05"+file+".png"

5. OCR

OK : magick '*.jpg' -crop 120x120+10+5 thumbnail%03d.png
DOESN'T WORK ! : $convert -crop x_sizexy_size+x_offset+y_offset inputfile outputfile
https://stackoverflow.com/questions/57530577/imagemagick-v7-and-cropping-tool
convert input.jpg -resize 800x600 -background black -compose Copy -gravity center -extent 800x600 output.jpg

"""
