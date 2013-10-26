
from myro import *
import math

init("COM40")
i = 0
j = 0
SPEED = 10.6 #m/s
ANGLE = 45 #degrees/s
sensor=[0,0,0]
time = 0 #time travelled in current heading
##ROTATE_EXTRA = ##X

destination = [int(raw_input), int(raw_input)]
current = [0.0, 0.0]
LEFT_OBSTACLE = 0
RIGHT_OBSTACLE = 0
offset_angle = 0
direct_angle= math.degrees(math.atan(destination[1]/destination[0]))

turnToHeading(direct_angle, ANGLE);
while math.fabs(current[0]-destination[0]) >= 5 and math.fabs(current[1]-destination[1]) >= 5:
    direct_angle=math.degrees(math.atan((destination[1]-current[1])/(destination[0]-current[0])))
    
    sensor = getObstacle()
    ##if sensor[0]<800 and sensor[1]<800 and sensor[2]<800:
    forward(1)

    if sensor[0]>=sensor[2]:
        turnRight(1)
        angle += ROTATE
        LEFT_OBSTACLE=1
    if sensor[0]<sensor[2]:   ##Turn a bit more to account for robot size
        if LEFT_OBSTACLE == 1:
            for j in range(0, ROTATE_EXTRA)
                turnRight(1)
                angle += ROTATE
        
            
        
    if sensor[2]>sensor[0]: 
        turnLeft(1)
        angle -= ROTATE
        RIGHT_OBSTACLE = 1
    if sensor[2]>=sensor[0]:         ##Turn a bit more to account for robot size
        if RIGHT_OBSTACLE = 1
            for j in range(0, ROTATE_EXTRA)
                turnLeft(1)
                angle -= ROTATE
            RIGHT_OBSTACLE=1
    
    i+=1
stop()

def turnToHeading (direct_angle, ANGLE):
    if (direct_angle>=0):
        turnLeft(direct_angle/ANGLE)
    else:
        turnRight(math.fabs(direct_angle)/ANGLE)

##def checkLeftObstacle:
    ##turnRight(90 degrees)
#    checkSensors()

##def timer(seconds=0):
##     """ A function to be used with 'for' """
##     start = time.time()
##     while True:
##         timepast = time.time() - start
##         if seconds != 0 and timepast > seconds:
##             raise StopIteration
##         yield round(timepast, 3)
## 
## _timers = {}
## def timeRemaining(seconds=0):
##     """ Function to be used with 'while' """
##     global _timers
##     if seconds == 0: return True
##     now = time.time()
##     stack = traceback.extract_stack()
##     filename, line_no, q1, q2 = stack[-2]
##     if filename.startswith("<pyshell"):
##         filename = "pyshell"
##     if (filename, line_no) not in _timers:
##         _timers[(filename, line_no)] = (now, seconds)
##         return True
##     start, duration = _timers[(filename, line_no)]
##     if seconds != duration:
##         _timers[(filename, line_no)] = (now, seconds)
##         return True
##     if now - start > duration:
##         del _timers[(filename, line_no)]
##         return False
##     else:
##         return True  
