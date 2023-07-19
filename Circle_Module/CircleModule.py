import math

circle = {
     "radius" : 0,
     "diameter" : 0,
     "circumference" : 0,
     "area" : 0
}

calcDiam = lambda r: 2 * r
calcCirc = lambda r: 2 * r * math.pi
calcArea = lambda r: r ** 2 * math.pi
radFormDiam = lambda d: d/ 2
radFromCirc = lambda c: c / (2 * math.pi)
radFromArea = lambda a: math.sqrt(a / math.pi)

def initCircle(rad):
    
    circle["radius"] = rad
    circle["diameter"] = calcDiam(rad)
    circle["circumference"] = calcCirc(rad)
    circle["area"] = calcArea(rad)