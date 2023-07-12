#!/usr/bin/python
#  A Python Program To Calculate The LCM and GCF of the numbers
# Author: Suhani Khare
# Date: July 11th' 2023

def gcf(num1, num2):
    ''' A funtion to take 2 parameters and computes the greatest common multiple of two '''

    factor = 1

    for i in range(1, num1):
        if ((num1 % i == 0) and (num2 % i == 0)):

            factor = i

    return (factor)


def lcm(num1, num2):
    ''' A function to take 2 parameters and computes '''

    factor = gcf(num1, num2)
    mult = (num1 * num2) // factor
    return (mult)


a = int(input("Please enter an interger\n"))
b = int(input("Please enter another integer\n"))

choice = input(
    "Do you want to get LCM or GCF of the numbers you just enered , pick lcm/gcf\n")

if (choice == "gcf"):
    greatestCF = gcf(a, b)
    print("Greatest Commom Factor", greatestCF)

elif (choice == "lcm"):
    leastCM = lcm(a, b)
    print("Lowest Common Multiple", leastCM)

else:
    print("Oops! Your choice is invalid,try again")
