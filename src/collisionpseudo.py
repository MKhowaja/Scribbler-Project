# Problem: center is x, y, not front of robot (cause when rotating that gets screwed up)
# TODO: use camera in decision making
from myro import *
import math

init("COM5")

x = 0
y = 0
theta = 0

x_f = 10
y_f = 10
r_f = 5

ir_rng = 0.1 # range of the IR sensor
threshold = 3200 # threshold for IR obstacle
v = 12.5 #cm/s
w = 90 # degrees/s

# until it reaches destination
while math.abs(x_f - x) > r_f || math.abs(y_f - y) > r_f:
	# rotate to face destination
	angle = getDeltaTheta()
	turn(angle)

	# move forward until detects obstacle
	while !obstructed(0):
		move(ir_rng)

	# turn based on which sensor detects the obstacle
	if getObstacle(0) > getObstacle(2):
		angle_turned = 90
	else:
		angle_turned = -90
	turn(angle_turned)

	# while its route back to the path is obstructed
	while obstructed(-angle_turned):
		if obstructed(0):
			turn(angle_turned)
		else:
			move(ir_rng)

	turn(-angle_turned) # get back on path
	move(ir_rng) # go past obstacle

def obstructed(n): # faces angle n, checks whether obstructed, turns back
	obstructed = False
	turn(n)
	if getObstacle(0) > threshold || sensor(1) > threshold || sensor(2) > threshold
		obstructed = True
	turn(-n)
	return obstructed


def turn(n): # rotates n degrees, updates theta
	if n >= 0:
		turnRight(1, n/w)
	else
		turnLeft(1, n/w)
	theta += n

def move(d): # moves d meters, updates position
	if d >= 0:
		forward(1, d/v)
	else:
		backward(1, d/v)
	
	x += d*cos(theta) # update x
	y += d*sin(theta) # update y

def getDeltaTheta(): # returns the angle between where it's facing and where it needs to go
	d_x = x_f - x
	d_y = y_f - y
	return math.degrees(math.atan(d_y/d_x))
