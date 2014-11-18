__author__ = 'Lacie'

def getBezierPoint(t, sx, sy, c1x, c1y, c2x, c2y, ex, ey):
	u = 1 - t
	tt = t * t
	uu = u * u
	uuu = uu * u
	ttt = tt * t
	px = sx * uuu
	py = sy * uuu
	px += 3 * uu * t * c1x
	py += 3 * uu * t * c1y
	px += 3 * u * tt * c2x
	py += 3 * u * tt * c2y
	px += ttt * ex
	py += ttt * ey
	return [ px, py ]
print "ayy"

k = 0.0
while k <= 1.0:
    print getBezierPoint(k,32,22,65,68,21,87,144,-56)
    k += 0.01