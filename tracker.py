from myro import *
import time, sys
import numpy
import matplotlib.pyplot as plt
import math
initialize("/dev/tty.IPRE6-185822-DevB")

'''we want to have states for the robot'''

FOUND = 1
LOOKING = 2

'''global variable declarations'''

TOLERANCE = 10
FOVangle = 20.56
SIZE = 0 
COLOR = (250, 250,250 )

'''method declarations'''

#gets the x and y distance from the object, so long as there are more than 1 picture

def getAngle(location, middle):
		diff = abs(location-middle)
		return 1.*diff/20.56

def getDistance(pictures, xprev):
		print "SIZE =", SIZE
		global FOVangle, SIZE, COLOR
		distance = [0, 0]
		if len(pictures) == 1:
				SIZE = getObjectSize(getTargets(pictures[0]))
		else:
				targets1 = getTargets(pictures[len(pictures)-1])
				targets2 = getTargets(pictures[len(pictures)-2])
				s1 = getObjectSize(targets1)
				s2 = getObjectSize(targets2)
				if s1 == -257 or s2 == -257:
						return distance
				else:
						distance[1] = SIZE*(1./s1 - 1./s2)
				x1 = getObjectLocation(targets2)[0]
				x2 = getObjectLocation(targets1)[0]
				a1 = getAngle(x1, 128)
				a2 = getAngle(x2, 128)
				distance[0] = math.tan(a2)*(distance[1] + xprev/math.tan(a1))/4

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
				if getX(p) == 130 and getY(p) == 112:
						print getRed(p), getGreen(p), getBlue(p)
				r = getRed(p)
				g = getGreen(p)
				b = getBlue(p)
				if abs(r - COLOR[0]) < TOLERANCE and abs(g - COLOR[1]) < TOLERANCE and abs(b - COLOR[2]) < TOLERANCE:
						targets.append(p)
#	print "target location", targets[len(targets)-1].getX(), targets[len(targets)-1].getY()
		return targets

def getCubic(location):
		cubics = [0,0]
		for i in range(2):
				p0 = location[len(location)-3][i]
				p1 = location[len(location)-2][i]
				m0 = p0-location[len(location)-4][i]
				m1 = location[len(location)-1][i]-p1
				a = -2*p1 + 2*p0 + 2*m0 + m1
				b = 3*p1 - 3*p0 - 3*m0 - m1
				c = m0
				d = p0
				cubics[i] = [a, b, c, d]
		return cubics

'''main declaration'''

def main():
		locations = []
		pictures = []
		dyvalues = []
		yvalues = [0] 
		xvalues = [0]
		for i in range(8):
				pictures.append(takePicture("color"))
				if len(locations) > 0:
						locations.append(getDistance(pictures, locations[len(locations)-1][0]))
				else:
						locations.append(getDistance(pictures, 0))
				print "x value", locations[len(locations)-1][0]
				savePicture(pictures[len(pictures)-1], "sample.jpg")
				print(locations[len(locations)-1][1])
				dyvalues.append(locations[len(locations)-1][1])
				yvalues.append(yvalues[len(yvalues)-1]+dyvalues[len(dyvalues)-1])
				xvalues.append(locations[len(locations)-1][0])
				if len(locations) >= 4:
						cubics = getCubic(locations)
						print cubics[0]
						print cubics[1]
		print "Y VALUES:", yvalues
		plt.figure(1)
		plt.subplot(211)
		plt.plot(yvalues)
		plt.subplot(212)
		plt.plot(xvalues)
		plt.show()

main()
