#!/usr/vin/python
# A Python program to create a unique values using SETS
# Author: Suhani Khare
# Date: July15th'2023

userSet = set()

print(type(userSet))

size = int(input("Please enter the size of the dataset you want to create\n"))

# Runing for loop to run the size times

for i in range(size):
    value = int(input("Please enter any value in here\n"))
    userSet.add(value)

# Traversing the dataset

print("Here is the userSet")
for i in userSet:
    print(i)

# Printing the original size and the length of theSET

print("Original Sie", size)
print("Length of the SET", len(userSet))
