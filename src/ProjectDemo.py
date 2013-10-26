from myro import *
import math

init("COM40")
i = 0
j = 0
SPEED = 10.6 #m/s
ANGLE = X #degrees/s
sensor=[0,0,0]
time = 0 #time travelled in current heading
ROTATE_EXTRA = ANGLE*1.2 ## to account for robot size, turn more than what the sensors detect to completely avoid object

destination = [int(raw_input), int(raw_input)]
current = [0.0, 0.0]
left = 0
right = 0
offset_angle = 0
direct_angle= math.atan(destination[1]/destination[0])
current_angle = 0
turnToHeading(direct_angle, current_angle, ANGLE);

while math.fabs(current[0]-destination[0]) >= 5 and math.fabs(current[1]-destination[1]) >= 5:
    direct_angle=math.atan((destination[1]-current[1])/(destination[0]-current[0]))
    
    sensor = getObstacle()
    #if sensor[0]<800 and sensor[1]<800 and sensor[2]<800:
    forward(1)

    if sensor[0]>=sensor[2]:
        turnRight(1)
        current_angle -= math.radians(ANGLE)
        left=1
        if sensor[0]<sensor[2]:         ##Turn a bit more to account for robot size
            for j in range(0, ROTATE_EXTRA)
                turnRight(1)
                current_angle-=math.radians(ANGLE)
        
            
        
    if sensor[2]>sensor[0]: 
        turnLeft(1)
        current_angle += math.radians(ANGLE)
        right = 1
        if sensor[2]>=sensor[0]:         ##Turn a bit more to account for robot size
            for j in range(0, ROTATE_EXTRA)
                turnLeft(1)
                current_angle += math.radians(ANGLE)

    current[0] += SPEED*math.cos(current_angle)
    current[1] += SPEED*math.sin(current_angle)
    
    i+=1
stop()

def turnToHeading (direct_angle, current_angle, ANGLE):
    if direct_angle>current_angle:
        turnRight((direct_angle-current_angle)/math.radians(ANGLE))
        current_angle=direct_angle
    elif direct_angle<current_angle:
        turnLeft((current_angle-direct_angle)/math.radians(ANGLE))
        current_angle=direct_angle
        

##def checkLeftObstacle:
    ##turnRight(90 degrees)
#    checkSensors()
