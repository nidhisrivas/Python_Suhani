#!/usr/bin/python
# A Python Program to calculate the cost the painting for a given room with fixed dimenssions

def getCost(length, width, height, windows, doors):
    ''' Some Cool Function to calculate the room paint cost'''

    ceilArea = width * height
    ceilCost = ceilArea * .25
    wallArea = 2 * (length * height + width * height)
    wallCost = wallArea * .5
    trimCost = 2 * windows + 3 * doors
    totalCost = ceilCost + wallCost + trimCost

    return (totalCost)


length = int(
    input("Please enter the length of the room you want to get painted\n"))
width = int(input("Please enter the width of the room you want to get painted\n"))
height = int(
    input("Please enter the height of the room you want to get painted\n"))
numWindows = int(
    input("Please enter how many windows are there in the room\n"))
numDoors = int(input("Please enter how many door are there in the room\n"))

roomCost = getCost(length, width, height, numWindows, numDoors)
print("Total charge of the room would be $", roomCost)
