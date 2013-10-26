# Problem: center is x, y, not front of robot (cause when rotating that gets screwed up)

x = 0
y = 0
theta = 0

x_f = 10
y_f = 10

	# until it reaches destination
	while(x != x_f && y != y_f) 
		# rotate to face destination
		angle = getDeltaTheta()
		turn(angle)

		# move forward until detects obstacle
		while(!obstructed(0))
			move(0.1) # 0.1 is the range of the sensor

		# turn based on which sensor detects the obstacle
		if(sensor(1) || sensor(2))
			angle_turned = 90
		if(sensor(3))
			angle_turned = -90
		turn(angle_turned)

		while(obstructed(-angle_turned))
			if(obstructed(0))
				turn(angle_turned)
			else
				move(0.1)

		move(0.1)

# use camera in decision making

def obstructed(n): # faces angle n, checks whether obstructed, turns back
	obstructed = False
	turn(n)
	if(sensor(1) || sensor(2) || sensor(3))
		obstructed = True
	turn(-n)
	return obstructed


def turn(n): # rotates n degrees, updates theta
	rotate(n)
	theta += n

def move(d): # moves d meters, updates position
	if(speed >= 0)
		forward(speed, time)
	else
		backward(speed,time)
	
	x += d*cos(theta) # update x
	y += d*sin(theta) # update y

def getDeltaTheta(): # returns the angle between where it's facing and where it needs to go
	delta_x = x_f - x
	delta_y = y_f - y
	return tan(delta_y/delta_x)	- theta
