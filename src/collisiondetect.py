from myro import *
init("COM40")
i = 0
sensor=[0,0,0]
while i<100:
    sensor = getObstacle()
    if sensor[0]<800 and sensor[1]<800 and sensor[2]<800:
        forward(1)

    elif sensor[0]>800 and sensor[2]<800:
        turnRight(1, 0.3)
        
    elif sensor[0]<800 and sensor[2]>800:
        turnLeft(1, 0.3)

    elif sensor[0]<800 and sensor[1]>800 and sensor[2]>800:
        turnLeft(1, 0.3)

    elif sensor[0]>800 and sensor[1]>800 and sensor[2]<800:
        turnRight(1, 0.3)
        
    else: 
        turnRight(1)
    i+=1
stop()


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
