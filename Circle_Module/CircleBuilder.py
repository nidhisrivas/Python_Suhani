import CircleModule as cM


radius = float(input("Please enter the radius of the circle\n"))

cM.initCircle(radius)

print("Radius: {}".format(radius))
print("Circle Diameter {}".format(cM.circle["diameter"]))
print("Circle Circumfrence  {}".format(cM.circle["circumference"]))
print("Circle Area  {}".format(cM.circle["area"]))

      

