#generally called when the Scribbler meets an obstacle
#returns True if the obstacle if a customer; returns False otherwise
#customer is an obstacle if more than a quarter of the picture is red/pink
def IsCustomer():
    picture = takePicture("color")  #takes picture of obstacle
    counter = 0 #variable for number of red 
    #loop for every pixel in photo
    for i in range(getWidth(picture)): 
        for j in range(getHeight(picture)):
            pixel = getPixel(picture, i, j) #read pixel
            #if pixel's colour is in range of colour (red)
            if getRed(pixel)>200 and getBlue(pixel)<55 and getGreen(pixel)<55:
                counter++ #add one to count
    #if more than 2/3 of photo matches colour
    if counter >= (2*getWidth(picture)*getHeight(picture)/3)
        return True
    else
        return False
