#!/usr/bin/python

import math

def toBase(number,base):
    alphabet = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    rems = []
    baseNum = ""
    orig = number
    print("NUMBER {}".format(number))
    
    while( number > 0):
        #print("Inside the while loop\n")
        rem = number % base
        if rem > 9: 
            rem = alphabet[rem]
        rems.insert(0,rem)
        number = number // base 
    #print("REMS :{}".format(rems)) 
    baseNum = str(orig) + " = "
    
    for item in rems:
        baseNum += str(item)
        
    return(baseNum)


def toDecimal(number,base):

    digits = []
    number = number.upper()
        
    #print(number)

    for digit in number:
        digits.insert(0, digit)

    sum = 0
    value = 0
    for i in range(len(digits)):
        digit = digits[i]
        ord_val = ord(digit)

        if 48 <= ord_val <= 57:
            value = ord_val - 48
        elif 65 <= ord_val <= 90:
            value = ord_val - 55
        else:
            print("Invalid number\n")
        
        sum += value * (base ** i)
        #print("sum", sum)
    return sum