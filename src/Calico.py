# TODO: use camera in decision making
# to do: check if it's continually getting further from the destination

#potential to dos:
    #smarter deciding turn left or right
    #assuming rectangular objects
    #instead of turning 90, turn to face destination
    #get velocity by doing move-by

# to do:
    # color recognition
    # music

from Myro import *
import math

init("COM7")

# initial position
x = 0
y = 0
theta = 90

# destination
x_f = 0
y_f = 100
theta_f = 90
r_f = 10 # radius of endzone

### CONSTANTS ###
ir_rng = 18 # range of the IR sensor (cm) (how far away it will notice an object)
threshold = 1000 # threshold for IR obstacle (anything greater is considered blocked)
v = 12.5 # velocity (cm/s)
#w = 115.38 # angular speed (omega) (degrees/s)

# Musical notes in the scale, as they correspond to beep frequency
# Notes are 4th and 5th octaves
#4th octave
A  = 440.0    #A
As = 466.164  # Asharp or Bflat
B  = 493.88   #B
#5th octave
C  = 523.25   #C 
Cs = 554.37   #Csharp or Dflat
D  = 587.33   #D
Ds = 622.25   #Dsharp or Eflat
E  = 659.26   #E
F  = 698.46   #F
Fs = 739.99   #Fsharp or Gflat
G  = 783.99   #G
Gs = 830.61   #G sharp or A flat
A2  = 880     #A octave higher
As2 = 932.33  #Asharp or Bflat octave higher
B2  = 987.77  #B octave higher

# setup
setIRPower(134)
setS2Volume(100)

# Play the song
def playSong():
    beep(0.25, B2)
    beep(0.25, A2)
    beep(0.5, G)
    beep(0.5, G)
    beep(0.5, G)

    beep(0.25, B)
    beep(0.25, C)
    beep(0.20, D)
    beep(0.20, E)
    beep(0.20, D)
    beep(0.20, B)
    beep(0.40, D)

    beep(0.25, G)
    beep(0.25, A2)
    beep(0.20, B2)
    beep(0.20, B2)
    beep(0.20, B2)
    beep(0.20, B2)
    beep(0.50, B2)

    beep(0.25, G)
    beep(0.25, A2)
    beep(0.20, B2)
    beep(0.20, A2)
    beep(0.20, A2)
    beep(0.20, Gs)
    beep(0.50, A2)

 
    beep(0.25, B2)
    beep(0.25, A2)
    beep(0.20, G)
    beep(0.20, A2)
    beep(0.20, G)
    beep(0.20, A2)
    beep(0.20, G)
    beep(0.20, D)

    beep(0.20, B)
    beep(0.20, C)
    beep(0.20, D)
    beep(0.20, E)
    beep(0.20, D)
    beep(0.20, B)
    beep(0.20, D)
    beep(0.20, D)

    beep(0.20, G)
    beep(0.20, A2)
    beep(0.7, B2)
    beep(0.8, A2)
    beep(1.1, G)

# Returns how much you need to turn by to face the final destination from the given angle
def getDeltaTheta(theta):
    global x, y
    d_x = x_f - x
    d_y = y_f - y
    if d_x == 0:
        if(d_y > 0):
            d_theta = 90
        else:
            d_theta = 270
    else:
        d_theta = math.degrees(math.atan(d_y/d_x))

    if(d_x < 0): # quandrant adjustment
        if(d_y < 0):
            d_theta -= 180
        else:
            d_theta += 180

    d_theta = d_theta - theta

    print ("Delta theta calculated to be:", d_theta)

    return d_theta

# Rotates n degrees, updates theta
def turn(n):
    global theta
    print ("Turning %d degrees..." % n)
    turnBy(n)
    theta += n

#Returns whether obstacle is red or not
def ColourDetect():
    picture = takePicture("color")  #takes picture of obstacle
    show(picture)
    counterr = 0 #variable for number of red
    #loop for every 100 pixels in photo
    for i in range((int)(getWidth(picture)/20)):
        for j in range((int)(getHeight(picture)/20)):
            pixel = getPixel(picture, 20*i, 20*j) #read pixel
            #if pixel colour is red
            if getBlue(pixel)<3*getRed(pixel)/5 and getGreen(pixel)<3*getRed(pixel)/5:
                counterr+=1 #add one to count
    #if more than 1/5 of photo matches colour
    if counterr > (getWidth(picture)*getHeight(picture)/2000):
        return True
    else:
        return False

# Faces angle n, checks whether obstructed, turns back
def obstructed(n):
    global threshold

    if n != 0:
        turn(n)

    obstruct = False

    num_readings = 8
    s = []
    for i in range(num_readings):
        s.append(getObstacle(1))
    s.sort()
    reading = s[int(num_readings/2 - 1)]

    if reading >= threshold:
        obstruct = True

    print ("Reading:%s, threshold:%d, obstruct?:%r" %(reading, threshold, obstruct))

    if n != 0:
        turn(-n)

    return obstruct

# Moves d centimeters, updates position
def move(d):
    global x, y, theta, v
    print ("Position before moving: x:%d y:%d theta:%d" % (x, y, theta))
    print ("Moving %d cm (%f seconds)..."%(d, abs(d/v)))
    if d >= 0:
        direction = 1
    else:
        direction = -1

    motors(direction,direction)
    t0 = currentTime()

    travelled = 0
    while not obstructed(0) and abs(travelled - d) > 5 and not atDest():
        t1 = currentTime()
        travelled += v*(t1-t0)*direction
        t0 = t1

    motors(0,0)

    if obstructed(0) and ColourDetect():
        playSong()

    x += travelled*math.cos(math.radians(theta)) # update x
    y += travelled*math.sin(math.radians(theta)) # update y
    print ("Position after moving: x:%d y:%d theta:%d" % (x, y, theta))

# Returns whether within radius of endzone
def atDest():
    return abs(x_f - x) < r_f and abs(y_f - y) < r_f

#### MAIN LOOP ####
x_f = int(raw_input("Enter final x"))
y_f = int(raw_input("Enter final y"))

# until it reaches destination
while not atDest():

    # rotate to face destination
    angle = getDeltaTheta(theta)
    turn(angle)

    # move forward until detects obstacle
    move(math.sqrt((x_f-x)**2+(y_f-y)**2))


    if atDest():
        print("Arrived at destination")
        turn(theta_f - theta)
        beep(1,880)
        break

    # turn based on which sensor detects the obstacle
    if getObstacle(0) < getObstacle(2):
        angle_turned = 90
    else:
        angle_turned = -90

    #raw_input("Press any key to continue...")
    turn(angle_turned)

    #raw_input("Press any key to continue...")
    move(ir_rng)

    # while its route back to the path is obstructed
    while obstructed(-angle_turned):
        #raw_input("Press any key to continue...")
        if obstructed(0):
            turn(angle_turned)
        else:
            move(ir_rng)

    move(ir_rng) # move once more for safety
    turn(-angle_turned) # turn back on path
    move(ir_rng*2) # move past obstacle

    # while its route back to the path is obstructed
    while obstructed(-angle_turned):
        #raw_input("Press any key to continue...")
        if obstructed(0):
            turn(angle_turned)
        else:
            move(ir_rng)
    
    move(ir_rng) # move once more for safety
    #raw_input("Press any key to continue...")

