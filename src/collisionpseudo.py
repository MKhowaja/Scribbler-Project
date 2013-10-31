# Problem: center is x, y, not front of robot (cause when rotating that gets screwed up)
# TODO: use camera in decision making

#noobnoobnoobnoobnub.
from myro import *
import math

init("COM5")

# position
x = 0
y = 0
theta = 0

# destination
x_f = 10
y_f = 10
r_f = 5 # radius of endzone

### CONSTANTS ###
ir_rng = 10 # range of the IR sensor (cm)
threshold = 500 # threshold for IR obstacle
v = 12.5 # velocity (cm/s)
w = 115.38 # omega (degrees/s)

def getDeltaTheta(): # returns the angle between where it's facing and where it needs to go
	global x, y
	d_x = x_f - x
	d_y = y_f - y
	d_theta = math.degrees(math.atan(d_y/d_x))
	print "Delta theta calculated to be:{}".format(d_theta) 
	return d_theta

def turn(n): # rotates n degrees, updates theta
	global w, theta
	print "Turning {} degrees ({} seconds)...".format(n, abs(n/w))
	if n >= 0:
		turnRight(1, n/w)
	else:
		turnLeft(1, -n/w)
	theta += n

def obstructed(n): # faces angle n, checks whether obstructed, turns back
	global threshold
	obstructed = False
	turn(n)
	print "sensor0:{}, sensor1:{}, sensor2:{}, threshold:{}".format(getObstacle(0), getObstacle(1), getObstacle(2), threshold)
	if getObstacle(0) > threshold or getObstacle(1) > threshold or getObstacle(2) > threshold:
		obstructed = True
	print "Obstructed!"
	turn(-n)
	return obstructed

def move(d): # moves d meters, updates position
	global x, y, theta, v
	print "Moving {}cm ({} seconds)...".format(d, abs(d/v));
	if d >= 0:
		forward(1, d/v)
	else:
		backward(1, -d/v)
	
	x += d*math.cos(theta) # update x
	y += d*math.sin(theta) # update y
	print "Position: x:{} y:{} theta:{}".format(x, y, theta)

# until it reaches destination
while abs(x_f - x) > r_f or abs(y_f - y) > r_f:
	# rotate to face destination
	angle = getDeltaTheta()
	turn(angle)

	# move forward until detects obstacle
	while not obstructed(0):
		move(ir_rng)

	# turn based on which sensor detects the obstacle
	if getObstacle(0) > getObstacle(2):
		angle_turned = 90
	else:
		angle_turned = -90
	turn(angle_turned)

	# while its route back to the path is obstructed
	while obstructed(-angle_turned):
		if getObstacle(1) > threshold:
			turn(angle_turned)
		else:
			move(ir_rng)

	turn(-angle_turned) # get back on path
	move(ir_rng) # go past obstacle
	raw_input("Press any key to continue...")
