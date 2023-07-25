#!/usr/bin/python

import random

def makeList(myList):

   i = 0
   while (i <= 100):
      num = random.randint(1,100)
      myList.append(num)
      i += 1
    
    
   return (myList)

#print(myList1)

#print(type(myTupple))
#print(myTupple)


