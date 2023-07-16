#!/usr/bin/python
# A Program to display the union and intersection feature of the SET
#Author : Suhani Khare
#Date: July 15th'2023

set1 = set()
set2 = set()

size1 = int(input("Please Enter the size of the set1\n"))
size2 = int(input("Please enter the size of the set2\n"))

for i in range(size1):
    value = input("Please enter any value for set1\n")
    set1.add(value)

for i in range(size2):
    value = input("Please enter any value for set2\n")
    set2.add(value)

setUnion= set1.union(set2)
setIntersection=set1.intersection(set2)


#Storing all the values
l1 = len(set1)
l2 = len(set2)
l3 = len(setUnion)
l4 = len(setIntersection)

#Printing all the values

print("Length of the SET1 :",l1)
print("SET1 : \n",set1)

print("Length of the SET2 :",l2)
print("SET2: \n",set2)
    
print("UNION of the set :")
print(setUnion)
print("length Union",l3)


print("INTERSECTION of the sets and its length is")
print(setIntersection)
print("length Intersection",l4)




