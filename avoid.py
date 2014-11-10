from myro import *
import math
initialize("/dev/tty.IPRE6-185822-DevB")
speak("what masterpiece shall we play today summoner?")

xpos = 0
found = False
around = False
distance = 0.45
turnAngle = 0.85
battery = getBattery()
print battery
leftTurn = 0.0341*battery*battery - 0.6035*battery + 3.2626
#leftTurn = 0.0346*battery*battery - 0.6035*battery + 3.2626
rightTurn = 0.118*battery*battery - 1.889*battery + 8.2643
#rightTurn = 0.118005*battery*battery - 1.889*battery + 8.2643
#rightTurn = 0.1182*battery*battery - 1.8899*battery + 8.2643
#leftTurn = 0.64
#rightTurn = 0.735


print "Right turn", rightTurn, "Left Turn", leftTurn

while True:
	left = getObstacle('left')
	center = getObstacle('center')
	right = getObstacle('right')
	print "left", left, "center", center, "right", right
	if left < 1100 and center < 1100 and not found:
		forward(distance*0.8, 1)
	else:
		if not found:
			speak("Brioso, brioso")
		found = True
		turnRight(1, rightTurn*0.98)
		forward(1, distance*0.7)
		turnLeft(1, leftTurn) 
		if not around:
			xpos += 1
	if found and left < 1100 and center < 1100: 
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
		forward(1, distance*2)
		turnLeft(1, leftTurn)		
	print "xpos:", xpos
#speak("adagio")
