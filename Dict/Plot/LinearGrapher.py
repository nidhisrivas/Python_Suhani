
import matplotlib.pyplot as plt

xVals = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

##yVals = ? Initialize the yVals list to hold appropriate y values to go with the x values
# What is the use of slope and yint here ? Are we suposed to pick any random list of yVals?
#slope = ?
#yint = ?

yVals = [3,5,7,9,11,13,15,17,19,21,23]
plt.plot(xVals,yVals,marker = 'X',ls = "dashed")
plt.grid()
plt.show()

