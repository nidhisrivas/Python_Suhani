import math

rectangle = {
   "length" : 0,
   "width" :  0,
   "diagnol" : 0,
   "perimeter" : 0,
   "area" : 0
}

calcPerim = lambda l, w: 2 * (l + w)
calcDiag = lambda l, w: math.hypot(l,w)
calcArea = lambda l, w: l * w

def initRectangle(length,width):
    rectangle["length"] = length
    rectangle["width"] = width
    rectangle["diagnol"] = calcDiag(length,width)
    rectangle["perimeter"] = calcPerim(length,width)
    rectangle["area"] = calcArea(length,width)