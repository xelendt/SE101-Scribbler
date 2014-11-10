from myro import *
import math
initialize("/dev/tty.IPRE6-185822-DevB")
speak("what masterpiece shall we play today summoner?")

xpos = 0
found = False
around = False
box = False
distance = 0.5
turnAngle = 0.85
battery = getBattery()
print battery
leftTurn = 0.03405*battery*battery - 0.6035*battery + 3.2626
#leftTurn = 0.0346*battery*battery - 0.6035*battery + 3.2626
rightTurn = 0.118005*battery*battery - 1.889*battery + 8.2643
#rightTurn = 0.1182*battery*battery - 1.8899*battery + 8.2643
#leftTurn = 0.64
#rightTurn = 0.735


print "Right turn", rightTurn, "Left Turn", leftTurn

while True:
	leftarray = []
	centerarray = []
	rightarray = []
	for i in range(3):
		leftarray.append(getObstacle('left'))
		centerarray.append(getObstacle('center'))
		rightarray.append(getObstacle('right'))
	left = (leftarray[0] + leftarray[1] + leftarray[2])/3
	center = (centerarray[0] + centerarray[1] + centerarray[2])/3
	right = (rightarray[0] + centerarray[1] + centerarray[2])/3
	print "left", left, "center", center, "right", right
	if left < 1100 and center < 1100 and not found:
		forward(distance, 1)
	else:
		if not found:
			speak("Brioso, brioso")
		found = True
		turnRight(1, rightTurn*0.985)
		forward(1, distance)
		turnLeft(1, leftTurn) 
		if not around:
			xpos += 1
	if found and left < 1000 and center < 1000: 
		'''if left > 600:
			turnRight(1, rightTurn)
			forward(1, 0.15)
			turnLeft(1, leftTurn)'''
		if around:
			while xpos > 0:
				forward(1, distance)
				xpos -= 1
			turnRight(1, rightTurn)
			forward(1, 1)
			break
		around = True
#		turnRight(1, rightTurn)
#		forward(1, 0.3)
#		turnLeft(1, leftTurn)
		forward(1, distance*2)
		turnLeft(1, leftTurn)		
	"xpos:", xpos
