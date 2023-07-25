import getColumn as gc
import matplotlib.pyplot as mpl


DataFile = "C:\\Users\\nidhi\\OneDrive\\Documents\\GitHub\\Python\\Dict\\Plot\\Dataset.csv"
heights = gc.getCol(DataFile,"Height")

heights = gc.getCol(DataFile,"Height")
mpl.xlabel("Height")
mpl.ylabel("Count")
mpl.hist(heights,edgecolor = "red",bins = 6)
mpl.show()


#import random
#heights = []
#for x in range(1000):
#    height = random.randint(140, 215)
#    heights.append(height)
#    
#jmpl.xlabel("Heights in CM")
#mpl.ylabel("Count")
#jmpl.hist(heights, edgecolor = "red", bins = 6)
#mpl.show()
