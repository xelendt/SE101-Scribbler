from myro import * 
import math 
initialize("/dev/tty.IPRE6-185822-DevB") 
 
while True:
'''     motors((math.cos(i)/10), (math.sin(i)/10))   i += 0.12''' 
		left = getObstacle('left') 
		center = getObstacle('center') 
	 	right = getObstacle('right') 
		if (left < 600 and center < 100 and right < 100): 
				forward(1, 1)
		else:
				turnRight(1, 0.8) 
				forward(1, 1) 
				turnLeft(1, 0.7) 
