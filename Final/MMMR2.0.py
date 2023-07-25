#!/usr/bin/python

import numpy
import statistics as st 

from Datasets import myList1 as ml
#from Datasets import myTupple as mt

print("You have chosen list from Dataset Module {}\n".format(ml))
#print("You have chosen tupple from Dataset Module {}\n".format(mt))
#print("You have chosen {} tupple dataset from Dataset Module\n".format(mt))

ml.sort()
#mt.sort()

min = ml[0]
max = ml[len(ml) - 1]
range = abs(max - min)
meanVal = numpy.mean(ml)
medianVal = numpy.median(ml)
modeVal = st.mode(ml)


print("Sorted List {} :".format(ml))
print("Mean Value : {:,.1f}".format(meanVal))
print("Median Value : {:,.2f}".format(medianVal))
print("Range Value : {}".format(range))
print("Mode Value : {}".format(modeVal))