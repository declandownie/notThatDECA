from array import array

def turn_right(robot, dir):
	robot.turn_right()
	dir = (dir+1)%4
	return dir

	
def control_robot(robot):
	""" control robot.

	Keyword arguments:
	robot -- Robot object that must be throught the maze

	"""
	"""rbtMap = [[-1 for i in xrange(100)] for i in xrange(100)] #square matrix to make life easier
	
	what the robot will see. it will map things out as it goes along.
	-1 = not detected yet/cannot reach (rbtMap is supposed to be arbitrarily larger than the actual map
	0 = coordinate with empty stuff
	1 = benign bug
	2 = benign bug with packet above it
	5 = the actual robot
	"""
	dir = 1;
	curX = 0 #current x pos
	curY = 0 #current y pos
	newVal = 0
	"""For its own map:
	when robot moves from one position to the next, it either collects all the items at that position
	or it leaves behind some. Ex. at pos(x,y), there was a benign bug (1). it collected that at pos(x,y) and moved on.
	Then it records that pos(x,y) is now 0 since the position is now empty.
	"""
	
	while robot.num_viruses_left() > 0:
		stepsF = robot.sense_steps(robot.SENSOR_FORWARD) #detect nearest wall forward
		stepsL = robot.sense_steps(robot.SENSOR_LEFT) #detect nearest wall to left
		stepsR = robot.sense_steps(robot.SENSOR_RIGHT) #detect nearest wall to right
		viruses_list = robot.sense_viruses()
		for vPos in range(0, len(viruses_list)):
			if vPos%2 != 0:
				if vPos > 0:
					robot.step_forward(vPos)
				elif vPos < 0:
					robot.step_backward(abs(vPos))
			else:
				if vPos > 0:
					robot.turn_right()
				elif vPos < 0:
					robot.turn_left()
				robot.step_forward(vPos)
				
			"""
			posX = int(pos[1:pos.index(",")])
			posY = int(pos[pos.index(",")+1:])
			if posX > 0:
				robot.step_forward(posX)
			elif posX < 0:
				robot.step_backward(posX)
			
			if posY > 0:
				robot.turn_right()
				robot.step_forward(posY)
			elif posY < 0:
				robot.turn_left()
				robot.step_forward(posY)
			"""