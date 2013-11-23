from Myro import *
import math

init("COM7")

num_readings = 8
threshold = 1050
setIRPower(132)

while True:
    s = []
    for i in range(num_readings):
        a = getObstacle()
        print ('%5d %5d %5d' % (a[0], a[1], a[2]))
        s.append(a[1])

    s.sort()
    mode = s[int(num_readings/2 - 1)]
    avg = sum(s)/float(len(s))
    print ('\t\t Median:' + repr(mode))
    print ('\t\t val:' + repr((mode+avg)/2))
