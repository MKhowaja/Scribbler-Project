from myro import *
import math

init("COM7")

num_readings = 8
threshold = 1050

while True:
	s = []
	for i in range(num_readings):
		a = getObstacle()
		print a
		s.append(getObstacle(1))
	s.sort()
	mode = s[num_readings/2 - 1]
	avg = sum(s)/float(len(s))
	print '\t\t Mode:' + repr(mode)
	print '\t\t val:' + repr((mode+avg)/2)
	#print '%5d %5d %5d' % (s[0], s[1], s[2])
