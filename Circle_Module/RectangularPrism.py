
import math

from RectangleModule import calcArea as aRect
from RectangleModule import calcDiag as diagRect

length = float(input("Please enter the length of the prism\n"))
width = float(input("Please enter the width of the prism\n"))
height = float(input("Please enter the height of the prism\n"))

frontBack = aRect(width,height) * 2
leftRight  = aRect(length,height) * 2
topBottom = aRect(length,width) * 2

surfaceArea = frontBack + leftRight + topBottom
baseDiag = diagRect(length,width)
diagonal = math.sqrt(baseDiag ** 2 + height ** 2)
volume = length * width * height 

print("Length : {}".format(length)+" Unit")
print("Width  :  {}".format(width)+" Unit")
print("Height :  {}".format(height)+" Unit")
print("Diagonal : {}".format(volume)+" Unit")
print("Surface Area : {}".format(surfaceArea)+" Sqr Unit")
print("Volume : Cube  {}".format(volume)+" Cube Unit")




