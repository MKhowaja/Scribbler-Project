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

# setup
setIRPower(134)
setS2Volume(100)

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

# Faces angle n, checks whether obstructed, turns back
def obstructed(n):
    global threshold
    if n != 0:
        turn(n)

    obstructed = False

    num_readings = 8
    s = []
    for i in range(num_readings):
        s.append(getObstacle(1))
    s.sort()
    reading = s[int(num_readings/2 - 1)]

    if reading >= threshold:
        obstructed = True

    print ("Reading:%s, threshold:%d, obstructed?:%r" %(reading, threshold, obstructed))

    if n != 0:
        turn(-n)

    return obstructed

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
