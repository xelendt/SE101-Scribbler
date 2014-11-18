from myro import *
import time, sys
import numpy
import matplotlib.pyplot as plt
initialize("/dev/tty.IPRE6-185822-DevB")

'''we want to have states for the robot'''

FOUND = 1
LOOKING = 2

'''global variable declarations'''

TOLERANCE = 60
FOVangle = 20.56
SIZE = 0 
COLOR = (255, 255, 60)

'''method declarations'''

#gets the x and y distance from the object, so long as there are more than 1 picture
def getDistance(pictures):
		print "SIZE =", SIZE
		global FOVangle, SIZE, COLOR
		distance = [0, 0]
		if len(pictures) == 1:
				SIZE = getObjectSize(getTargets(pictures[0]))
		else:
				s1 = getObjectSize(getTargets(pictures[len(pictures)-1]))
				s2 = getObjectSize(getTargets(pictures[len(pictures)-2]))
				if s1 == -257 or s2 == -257:
						return distance
				else:
						distance[1] = SIZE*(1./s1 - 1./s2)
		return distance

#gets the size of the object of color in the picture 				
def getObjectSize(targets):
		if len(targets) > 0:
				largest = 0
				smallest = 257
				for t in targets:
						if getX(t) > largest:
								largest = getX(t)
						if getX(t) < smallest:
								smallest = getX(t)
#		print "largest", largest
#		print "smallest", smallest
				print "size", largest-smallest
				return largest-smallest
		else:
				return -257

#gets the object's location		
def getObjectLocation(targets):
		location = [0, 0]
		if len(targets) > 0:
				for t in targets:
						location[0] += getX(t)
						location[1] += getY(t)
				location[0]/=len(targets)
				location[1]/=len(targets)
		return location

#finds the target colors in the picture
def getTargets(picture):
		global COLOR, TOLERANCE
		targets = []
		pixels = getPixels(picture)
		for p in pixels:
				if getX(p) == 127 and getY(p) == 127:
						print getRed(p), getGreen(p), getBlue(p)
				r = getRed(p)
				g = getGreen(p)
				b = getBlue(p)
				if abs(r - COLOR[0]) < TOLERANCE and abs(g - COLOR[1]) < TOLERANCE and abs(b - COLOR[2]) < TOLERANCE:
						targets.append(p)
#	print "target location", targets[len(targets)-1].getX(), targets[len(targets)-1].getY()
		return targets

def getCubic(locations):
		pass

'''main declaration'''

def main():
		locations = []
		pictures = []
		dyvalues = []
		yvalues = [0] 

		for i in range(5):
				pictures.append(takePicture("color"))
				locations.append(getDistance(pictures))
				savePicture(pictures[len(pictures)-1], "sample.jpg")
				print(locations[len(locations)-1][1])
				dyvalues.append(locations[len(locations)-1][1])
				yvalues.append(yvalues[len(yvalues)-1]+dyvalues[len(dyvalues)-1])
		print "Y VALUES:", yvalues
		plt.plot(yvalues)
		plt.show()

main()
