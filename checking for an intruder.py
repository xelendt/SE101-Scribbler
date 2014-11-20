from myro import *
initialize("/dev/tty.IPRE6-185822-DevB")
def check():
    pinks = [[156, 34, 93], [219,48,130], [255, 8, 127], [255, 56, 152], [255, 84, 167],
             [255, 113, 181], [228, 35, 157], [232, 64, 170], [236, 93, 183],
             [231, 161, 176]]
    
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
                if pinks[a][0]*0.95 <= red <= 1.05*pinks[a][0]:
                    if pinks[a][1]*0.95 <= green <= 1.05*pinks[a][1]:
                        if pinks[a][2]*0.95 <= blue <= 1.05*pinks[a][2]:             
                            return True
    return False

def surveillance():
    turnLeft(0.3, 1)
    if check():
        return 1 
		
while True:
	if surveillance():
			speak("INTRUDER")
