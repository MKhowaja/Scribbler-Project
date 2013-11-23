# Problem: center is x, y, not front of robot (cause when rotating that gets screwed up)
# TODO: use camera in decision making
# to do: check if it's continually getting further from the destination

from Myro import *
import math

init("COM7")

# position
x = 0
y = 0
theta = 90

# destination
x_f = 0
y_f = 200
r_f = 10 # radius of endzone

### CONSTANTS ###
ir_rng = 13 # range of the IR sensor (cm)
threshold = 1000 # threshold for IR obstacle
v = 12.5 # velocity (cm/s)
w = 115.38 # omega (degrees/s)

def getDeltaTheta(): # returns the angle between where it's facing and where it needs to go
    global x, y, theta
    d_x = x_f - x
    d_y = y_f - y
    if d_x == 0:
        if(d_y > 0):
            d_theta = 90
        else:
            d_theta = 270
    else:
        d_theta = math.degrees(math.atan(d_y/d_x))

    print ("Delta theta calculated to be:", (d_theta - theta))
    if(d_x >= 0):
        return (d_theta - theta)
    else:
        return (d_theta + theta)

def turn(n): # rotates n degrees, updates theta
    global theta
    print ("Turning %d degrees..." % n)
    turnBy(n)
    theta += n

def obstruct():
    obstructed = False

    num_readings = 8
    s = []
    for i in range(num_readings):
        s.append(getObstacle(1))
    s.sort()
    reading = s[int(num_readings/2 - 1)]

    print ("Reading:%s, threshold:%d" %(reading, threshold))
    if reading >= threshold:
        obstructed = True
    if obstructed:
        print ("Obstructed!")

    return obstructed

def obstructed(n): # faces angle n, checks whether obstructed, turns back
    global threshold
    if n != 0:
        turn(n)

    blocked = False
    blocked = obstruct()

    if n != 0:
        turn(-n)
    return blocked

def move(d): # moves d centimeters, updates position
    global x, y, theta, v
    print ("Moving %d cm (%f seconds)..."%(d, abs(d/v)))
    if d >= 0:
        forward(1, d/v)
    else:
        backward(1, -d/v)

    print ("Initial position: x:%d y:%d theta:%d" % (x, y, theta))
    x += d*math.cos(math.radians(theta)) # update x
    y += d*math.sin(math.radians(theta)) # update y
    print ("Final position: x:%d y:%d theta:%d" % (x, y, theta))

def atDest():
    return abs(x_f - x) < r_f and abs(y_f - y) < r_f

# until it reaches destination
while not atDest():
    # rotate to face destination
    angle = getDeltaTheta()
    turn(angle)

    # move forward until detects obstacle
    while not obstructed(0) and not atDest():
        raw_input("Press any key to continue...")
        move(ir_rng)

    if atDest():
        break

    # turn based on which sensor detects the obstacle
    if getObstacle(0) > getObstacle(2):
        angle_turned = -90
    else:
        angle_turned = 90
    raw_input("Press any key to continue...")
    turn(angle_turned)

    raw_input("Press any key to continue...")

    move(ir_rng)

    # while its route back to the path is obstructed
    while obstructed(-angle_turned):
        raw_input("Press any key to continue...")
        if obstructed(0):
            turn(angle_turned)
        else:
            move(ir_rng)

    move(ir_rng) # move once more for safety
    turn(-angle_turned) # get back on path
    move(ir_rng*2) # move once more for safety

    # while its route back to the path is obstructed
    while obstructed(-angle_turned):
        raw_input("Press any key to continue...")
        if obstructed(0):
            turn(angle_turned)
        else:
            move(ir_rng)
    
    move(ir_rng) # move once more for safety

    raw_input("Press any key to continue...")
