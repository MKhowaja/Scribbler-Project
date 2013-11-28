#generally called when the Scribbler meets an obstacle
from Myro import *

init("COM7")
def ColourDetect():
    picture = takePicture("color")  #takes picture of obstacle
    show(picture)
    counterr = 0 #variable for number of red 
    counterg = 0 #variable for number of green
    #loop for every pixel in photo
    for i in range(getWidth(picture)): 
        for j in range(getHeight(picture)):
            pixel = getPixel(picture, i, j) #read pixel
            #if pixel colour is red
            if getBlue(pixel)<3*getRed(pixel)/5 and getGreen(pixel)<3*getRed(pixel)/5:
                counterr+=1 #add one to count
    #if more than 1/5 of photo matches colour
    if counterr > (getWidth(picture)*getHeight(picture)/5):
        return True
    else:
        return False

ColourDetect()