import math

square = {
         "side" : 0,
         "diagonal" : 0,
         "perimeter" : 0,
         "area" : 0
}

calcDiag = lambda s: math.hypot(s,s)
calcPerim = lambda s: 4 * s
calcArea = lambda s: s ** 2
sideFromDiag = lambda d: math.sqrt(d ** 2 / 2)
sideFromPerim = lambda p: p / 4
sideFromArea = lambda a: math.sqrt(a)

def initSquare(side):
    square["side"] = side
    square["diagonal"] = calcDiag(side)
    square["perimeter"] = calcPerim(side)
    square["area"] = calcArea(side)
