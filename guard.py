'''TODO
 - find an object
	To do this we can do 1 of 2 things (OHHH CDM)
	- find specific colors
	- find edges, so to see the outline of an object based on difference in hue and saturation
 - chase the object
	- turns toward the object 
	- moves in direction
 - yells at objects
	- when object is large enough, speaks through computer
 - doesn't run into obstacles
	- while running toward object, uses IR sensors to avoid objects
 - if person says password, robot shuts off
'''

from myro import *
import random, time, sys

initialize("/dev/tty.IPRE6-185822-DevB")

tolerance = 40

target = (255, 255, 0)

while True:
	location = [0, 0]
	picture = takePicture("color")
	width = getWidth(picture)
	height = getHeight(picture)
	middle = width/2.
	targets = [(middle, height/2)]
	pixels = getPixels(picture)
	for p in pixels:
		r = getRed(p)
		g = getGreen(p)
		b = getBlue(p)
		if abs(r - target[0]) < tolerance and abs(g - target[1]) < tolerance and abs(b - target[2]) < tolerance:
			targets.append(p)
			location[0] += getX(p)
			location[1] += getY(p)
		#	print r, g, b
#	for p in targets:
#		location[0] += getX(p)
#		location[1] += getY(p)
	location[0]/=len(targets)
	location[1]/=len(targets)
			
	print "x: ", location[0], "y: ", location[1]
	
	angle = location[0] - middle
	print angle

	if abs(angle) > 20:
		if angle > 0:
			turnRight(0.3, abs(angle/width))	
		else:
			turnRight(-0.3, abs(angle/width))	
	else:
		forward(1, 1)

