import CircleModule
import RectangleModule

from CircleModule import calcCirc as cirCum
from RectangleModule import calcArea as rectArea

radius = float(input("Please enter the radius of the cylinder\n"))
height = float(input("Please enter height of the Cylinder\n"))

baseArea = CircleModule.calcArea(radius)
lateralArea = cirCum(radius) * height

#OR (If Using Rectangular Module)
#lateralArea = rectArea(cirCum(radius),height)

surfaceArea = lateralArea + 2  * baseArea
volume = baseArea * height
print("Radius : {}".format(radius)+" Units")
print("Height : {}".format(height)+" Units")
print("Surface Area : {}".format(surfaceArea)+" Square Units")
print("Volume : {}".format(volume)+" Cube Units")
