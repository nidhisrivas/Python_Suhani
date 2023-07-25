#we are going to be looking at the datasets
#mean - average of the dataset
#median - 
#mode
#range

import numpy
from scipy import stats


dataset = [16,88,96,21,29,3,25,84,85,30,84,79,48,89,64,34,54,91,35,12]

print(dataset)
# Sort using .sort()
print(dataset)
dataset.sort()
print("Sorted Dataset : {}".format(dataset))
# if you want descending order, .sort(reserve = True)

dataset.sort(reverse=True)
print("Descending Dataset: {}".format(dataset))

averageVal = numpy.mean(dataset)
print("Average: {:.2f}".format(averageVal))
## Median
## Mode




# Range -  the deiffrence between smallets and largest values
firstVal = dataset[0]
lastVal = dataset[len(dataset) - 1]
range = abs(firstVal - lastVal)
print("Range: {}")
range = abs(firstVal - lastVal)
print("Range: {}".format(range))
