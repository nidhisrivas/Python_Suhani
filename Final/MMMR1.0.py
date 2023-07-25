

import numpy
import statistics as st

dataset = []
size = int(input("Please enter the size of the dataset\n"))

for i in range(size):
  num = int(input("Please enter any number you want to add in dataset\n"))
  dataset.append(num)
print("Unsorted Dataset: {}".format(dataset))
#Sort the dataset

dataset.sort()
print("Sorted Dataset: {}".format(dataset))
min = dataset[0]
#size is len(dataset), so we can use size

max = dataset[size - 1]
range = abs(max - min)
meanVal = numpy.mean(dataset)
medianVal = numpy.median(dataset)
modeVal = st.mode(dataset)
print("Range : {}".format(range))
print("Mean : {}".format(meanVal))
print("Median: {}".format(medianVal))
print("Mode : {}".format(modeVal))
