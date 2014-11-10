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
leftTurn = 0.0346*battery*battery - 0.6035*battery + 3.2626
#leftTurn = 0.0346*battery*battery - 0.6035*battery + 3.2626
rightTurn = 0.1178*battery*battery - 1.8899*battery + 8.2643
#rightTurn = 0.1182*battery*battery - 1.8899*battery + 8.2643
leftTurn = 0.64
rightTurn = 0.735


print "Right turn", rightTurn, "Left Turn", leftTurn

while True:
	left = getObstacle('left')
	center = getObstacle('center')
	right = getObstacle('right')
	print "left", left, "center", center, "right", right
	if left < 1020 and center < 1020 and not found:
		forward(distance, 1)
	else:
		turnRight(1, rightTurn*0.985)
		forward(1, 2.2)
		turnLeft(1, leftTurn)
		forward(1, 4)
		turnLeft(1, leftTurn)
		forward(1, 4)
		turnRight(1, rightTurn)
		forward(1, 1)
		break
