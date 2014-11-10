from myro import *
import random, time, sys

initialize("/dev/tty.IPRE6-185822-DevB")

tolerance = 40

target = (0 ,0, 0)

while True:
	targets = []
	location = [0, 0]
	picture = takePicture("color")
	width = getWidth(picture)
	height = getHeight(picture)
	middle = width/2.
	pixels = getPixels(picture)
	for p in pixels:
		r = getRed(p)
		g = getGreen(p)
		b = getBlue(p)
		if abs(r - target[0]) < tolerance and abs(g - target[1]) < tolerance and abs(b - target[2]) < tolerance:
			targets.append(p)
		#	print r, g, b
	for p in targets:
		location.x += getX(p)
		location.y += getY(p)
	location[0]/=len(targets)
	location[1]/=len(targets)
			
	print "x: ", location[0], "y: ", location[1]
	
	angle = location[0] - middle

	turnRight(0.3, angle/width*20.)	
