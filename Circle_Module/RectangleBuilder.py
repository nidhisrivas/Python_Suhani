

from CircleModule import calcArea as cA
from CircleModule import calcCirc as cC
from RectangleModule import calcArea as rA

radius = float(input("PLease enter radius of the cylinder\n"))
height = float(input("Please enter height of the cylinder\n"))

baseArea = cA(radius)
lateralArea = cC(radius) * height

surfaceArea = lateralArea + 2 * baseArea
volume = baseArea * height

print("Radius {} Unit".format(radius))
print("Height {} Unit ".format(height))
print("Surface Area {} UnitSquare".format(surfaceArea))
print("Volume {} UnitCube".format(volume))




               