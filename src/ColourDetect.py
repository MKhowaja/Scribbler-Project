#generally called when the Scribbler meets an obstacle
def ColourDetect():
    beep(1,880) #beep at beginning
    picture = takePicture("color")  #takes picture of obstacle
    counterr = 0 #variable for number of red 
    counterg = 0 #variable for number of green
    #loop for every pixel in photo
    for i in range(getWidth(picture)): 
        for j in range(getHeight(picture)):
            pixel = getPixel(picture, i, j) #read pixel
            #if pixel colour is red
            if getRed(pixel)>200 and getBlue(pixel)<55 and getGreen(pixel)<55:
                counterr++ #add one to count
            #if pixel colour is green
            if getRed(pixel)<55 and getBlue(pixel)<55 and getGreen(pixel)<200:
                counterg++ #add one to count
    #if more than 2/3 of photo matches colour
    if counterr >= (2*getWidth(picture)*getHeight(picture)/3)
        beep(1,880) #beep at end
        return 1
    elif counterg >= (2*getWidth(picture)*getHeight(picture)/3)
        beep(1,880) #beep at end
        return 2
    else
        beep(1,880) #beep at end
        return 0
