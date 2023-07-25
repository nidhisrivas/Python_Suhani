
import math 
import numpy
import statistics as st 
import Datasets 

size = int(input("Please enter the size of the dataset\n"))
dataset = []

for x in range(size):
    value = int(input("Enter the value of the dataset\n"))
    dataset.append(value)
dataset.sort()
print(dataset)

sd = numpy.std(dataset)
vari = st.variance(dataset)
perc = int(input("Enter the percentile you are intrested\n"))
percVal = math.floor(numpy.percentile(dataset,perc))

print("Standar Deviation: {:.2f}".format(sd))
print("Variance: {:.2f}".format(vari))
print("Variane: {:.2f}".format(vari))
print("The {0}th percentile is {1},meaning {0}% of values are {1} or less.".format(perc,percVal))
      

