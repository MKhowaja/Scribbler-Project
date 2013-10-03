from myro import *
init("COM40")
def main():
    ##rSetForwardnessTxt("fluke-forward");
    int i = 0;
    ##loop to stop at the second obstacle seen
    while(i<2):
        Forward(1,1)
        if (rGetObstacleNum(1)>800):
            rTurnRight(1,1)
            i++

        stop()

  
main()
