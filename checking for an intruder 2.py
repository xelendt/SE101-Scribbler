from myro import *
initialize("/dev/tty.IPRE6-185822-DevB")
def check():
    white = [[255, 255, 255], [150,148,159], [207, 202, 215], [211, 207, 221], [242, 236, 247]]
        
    p = takePicture("color")
    width = getWidth(p)
    height = getHeight(p)
    for i in range(0, width):
        for j in range(0, height):
            pixel = getPixel(p, i, j)
            red = getRed(pixel)
            blue = getBlue(pixel)
            green  = getGreen(pixel)
            for a in range(len(pinks)):
                if white[a][0]*0.95 <= red <= 1.05*white[a][0]:
                    if white[a][1]*0.95 <= green <= 1.05*white[a][1]:
                        if white[a][2]*0.95 <= blue <= 1.05*white[a][2]:             
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
