from myro import *
initialize("/dev/tty.IPRE6-185822-DevB")
def check():
    white = [[255, 255, 255], [207, 202, 215], [211, 207, 221], [242, 236, 247]]

    tolerance = 10    
    p = takePicture("color")
    savePicture (p, "sample.jpg")
    width = getWidth(p)
    height = getHeight(p)
    for i in range(0, width):
        for j in range(0, height):
            pixel = getPixel(p, i, j)
            red = getRed(pixel)
            blue = getBlue(pixel)
            green  = getGreen(pixel)
            for a in range(len(white)):
			    if 255-red < tolerance and 255-blue < tolerance and 255-green < tolerance:
				    return True
    return False

def surveillance():
    turnLeft(0.3, 1)
    if check():
        return True 
    return False
		
while True:
	if surveillance():
			speak("INTRUDER")
			break
