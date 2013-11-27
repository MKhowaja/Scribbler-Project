#generally called when the Scribbler meets an obstacle
#returns True if the obstacle if a customer; returns False otherwise
#customer is an obstacle if more than a quarter of the picture is red/pink
def IsCustomer():
    obstacle = takePicture("color")
    counter = 0
    for i in range(getWidth(picture)):
        for j in range(getHeight(picture)):
            pixel = getPixel(picture, i, j)
            #if pixel's colour is in range of colour (pink/red in this case)
            if getRed(pixel)>200:
                counter++
    if counter >= (getWidth(picture)*getHeight(picture)/4)
        return True
    else
        return False
