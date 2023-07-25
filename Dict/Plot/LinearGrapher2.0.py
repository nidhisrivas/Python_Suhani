
import matplotlib.pyplot as plt

slope = float(input("Please enter any number as slope\n"))
yint = int(input("PLease enter nay value as Y intercept\n"))

xVals = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
yVals = []

for num in xVals:
    yint = slope * num + yint
    
    yVals.append(num)

plt.plot(xVals,yVals,marker = 'o',ls = 'dotted')
plt.grid()
plt.show()



