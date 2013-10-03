from myro import *
init("COM40")
def main():
    int i = 0
    ##loop to stop at the second obstacle seen
    while(i<2):
        Forward(1,1)
        if (getObstacle(1)>800):
            turnRight(1,1)
            i++

        stop()

  
main()
