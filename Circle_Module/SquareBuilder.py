import SquareModule as sq

sideLength = float(input("Enter the length of the square\n"))
sq.initSquare(sideLength)
print("Side LEngth: {}".format(sq.square["side"]))
print("Perimeter: {}".format(sq.square["perimeter"]))
print("Area: {}".format(sq.square["area"]))
print("Diagonal: {}".format(sq.square["diagonal"]))


