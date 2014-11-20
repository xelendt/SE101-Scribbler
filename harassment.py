from myro import *
import random, time, sys

width = 256
height = 192

initialize("/dev/tty.IPRE6-185822-DevB")

tolerance = 20 #tolerance of the color

target = (255, 255, 255) #target color

while True:
	location = [0, 0] #location of the target
	picture = takePicture("color") 
	savePicture(picture, "sample.jpg")
	width = getWidth(picture)
	height = getHeight(picture)
	middle = width/2.
	targets = [] #array of all of the pixels of the color we are looking for
	pixels = getPixels(picture)
	for p in pixels:
		r = getRed(p)
		g = getGreen(p)
		b = getBlue(p)
		if abs(r - target[0]) < tolerance and abs(g - target[1]) < tolerance and abs(b - target[2]) < tolerance:
			targets.append(p)
			location[0] += getX(p)
			location[1] += getY(p)
	# to find the center of the target, take the average of all the pixels
	if (len(targets) > 0):
		location[0]/=len(targets)
		location[1]/=len(targets)
		
	print "target location:"	
	print "x: ", location[0], "y: ", location[1]
	
	angle = location[0] - middle
	print "angle: ",angle

	#if none of the colors are found, then we turn and look for some
	if len(targets) > 0:
		#if the target is straight ahead, move forward
		#otherwise, turn toward object
		if abs(angle) > 20:
			if angle > 0:
				turnRight(0.3, abs(angle/width))	
			else:
				turnRight(-0.3, abs(angle/width))	
		# use IR sensors to check whether the robot is going to run into the object
		# if it won't, move forward and otherwise, we found the object	 
		else:
			left = getObstacle('left')
			center = getObstacle('center')
			right = getObstacle('right')
			obstruction = left + right + center
			if obstruction < 2000:
				forward(0.5, 1)
			else:
				speak("stranger danger")
	else:
		turnRight(0.5, 1)

