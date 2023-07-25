#!/usr/bin/python

import random

from ListSorterModule import sortAscBubble as ascBub
from ListSorterModule import sortDescBubble as descBub
from ListSorterModule import sortAscExchange as ascExc
from ListSorterModule import sortDescExchange as descExc
from ListSorterModule import sortAscInsertion as ascIns
from ListSorterModule import sortDescInsertion as descIns
from ListSorterModule import sortAscSelection as ascSel
from ListSorterModule import sortDescSelection as descSel
from RadomDataSetModule import makeList as mkL


dataset = []

## Mr R, I'm little unclear from the instructions as using the RandaomDataSetModule, so adding a third choice if user chooses to enter a random dataset from the RandomDSModule's makelist.
## We can go over this tomorrow.Thanks  -- Suhani
choice = int(input("Choose:\n1 - Enter Your Own Dataset\n2 - Use a Random Dataset\n3- Use RandomData Set from MakeList Funtion of RandDS\n"))
if choice == 1:
  size = int(input("Enter size of dataset: "))
  for x in range(size):
    num = int(input("Enter a value: "))
    dataset.append(num)
elif choice == 2:
  size = int(input("Enter size of dataset: "))
  for x in range(size):
    num = random.randint(1, 100)
    dataset.append(num)

elif choice == 3:
   dataset = mkL(dataset)
   
print(dataset)

dataset2 = ascBub(dataset)
print("-" * 50)
print("Ascending Bubble: {}".format(dataset2))
dataset3 = descBub(dataset)
print("Descending Bubble: {}".format(dataset3))
print("-" * 50)
dataset4 = ascExc(dataset)
print("Ascending Exchange: {}".format(dataset4))
dataset5 = descExc(dataset)
print("Descending Exchange: {}".format(dataset5))
print("-" * 50)
dataset6 = ascIns(dataset)
print("Ascending Insertion: {}".format(dataset6))
dataset7 = descIns(dataset)
print("Descending Insertion: {}".format(dataset7))
print("-" * 50)
dataset8 = ascSel(dataset)
print("Ascending Selection: {}".format(dataset8))
dataset9 = descSel(dataset)
print("Descending Selection: {}".format(dataset9))
print("-" * 50)
print(dataset)