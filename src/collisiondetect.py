from myro import *
init("COM40")
i = 0
##loop to stop at the second obstacle seen
while i<100:
    forward(1)
    while getObstacle(1)>750:
        turnRight(1)
        
    i+=1
stop()

  
