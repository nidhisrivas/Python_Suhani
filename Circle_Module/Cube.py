
from SquareModule import calcArea as sqA
from SquareModule import calcDiag as sqDia 


side = float(input("Please enter the side of the cube\n"))
surfaceArea = sqA(side) * 6 
volume = side ** 3
diagonal =  3 ** 1/2 * side

print("Side: {}".format(side))
print("Diagonal: {}".format(diagonal))
print("Surface Area: {}".format(side))
print("Volume: {}".format(volume))








