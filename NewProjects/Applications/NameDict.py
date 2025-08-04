#!/usr/bin/env python3
# name: NameDict.py
# This script collects names and ages from the user and stores them in a dictionary.

ageList = []
nameList = []
count = 0
while(count<5): 
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    nameList.append(name)
    ageList.append(age)
    count += 1


nameAge = {
 nameList[0] : ageList[0],
 nameList[1] : ageList[1],
 nameList[2] : ageList[2],
 nameList[3] : ageList[3],
 nameList[4] : ageList[4]
}

print(" ")
for val in nameAge:
    print("Name: {} , Age: {}".format(val,nameAge[val]))
    #print(f"Here is the name and age: {val} is {nameAge[val]} years old")
# This code collects names and ages from the user, stores them in a dictionary, and prints the results.




    #DIFFERENT PROGRAM: csv File: firstnamem last name, age, print first name and age