from myro import *
import math

init("COM40")
j = 0
SPEED = 10.6 #cm/s
ANGLE = X #degrees/s
sensor=[0,0,0]
time = 0 #time travelled in current heading
ROTATE_EXTRA = ANGLE*T #T is some time TBD

destination = [int(raw_input)*100, int(raw_input)*100]  #destination coordinates (convert to cm)
current = [0.0, 0.0]    #current coordinates (will be incremented by cm)
obstacle = 0    #variable to see if robot is moving past an obstacle
direct_angle = math.atan(destination[1]/destination[0])  #angle towards destination
current_angle = 0   #angle the robot is facing
turnToHeading(direct_angle, current_angle, ANGLE)

while math.fabs(current[0]-destination[0]) >= 5 and math.fabs(current[1]-destination[1]) >= 5: #move until scribby is 5cm away
    direct_angle=math.atan((destination[1]-current[1])/(destination[0]-current[0]))     #Track angle towards destination
    sensor = getObstacle()
    if sensor[0]<500 and sensor[1]<500 and sensor[2]<500:   #If path is clear, move forward and track coordinates
        forward(1)
        current[0] += SPEED*math.cos(current_angle)
        current[1] += SPEED*math.sin(current_angle)
        if obstacle == 1         #If it just turned from an obstacle, try to turn back towards destination
            obstacle = 0
            turnToHeading(direct_angle, current_angle, ANGLE)
    elif sensor[0]>=sensor[2]:      #If obstacle to left, turn right and track angle
        turnRight(1)
        current_angle -= math.radians(ANGLE)
        obstacle = 1
        if sensor[0]<sensor[2]:         #Turn a bit more to account for robot size
            for j in range(0, ROTATE_EXTRA)
                turnRight(1)
                current_angle-=math.radians(ANGLE)
    elif sensor[2]>sensor[0]:       #If obstacle to right, turn left and track angle
        turnLeft(1)
        current_angle += math.radians(ANGLE)
        obstacle = 1
        if sensor[2]>=sensor[0]:         #Turn a bit more to account for robot size
            for j in range(0, ROTATE_EXTRA)
                turnLeft(1)
                current_angle += math.radians(ANGLE)
stop()

def turnToHeading (direct_angle, current_angle, ANGLE):     #turn robot towards destination
    if direct_angle>current_angle:
        turnRight((direct_angle-current_angle)/math.radians(ANGLE))
        current_angle=direct_angle
    elif direct_angle<current_angle:
        turnLeft((current_angle-direct_angle)/math.radians(ANGLE))
        current_angle=direct_angle
        

#def checkLeftObstacle:
    ##turnRight(90 degrees)
#    checkSensors()
