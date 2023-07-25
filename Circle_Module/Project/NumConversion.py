#!/usr/bin/python

import math
import NumberConverter as nC


choice = int(input("Please pick a choice\nTo convert to decimal 1\nTo convert to base 2\n"))
if( choice == 1 ):
    num = input("Please enter any number\n")
    base = int(input("Please enter any base\n"))
    
    if (2 <= base <= 36):
        result = nC.toDecimal(num,base)
        print("Converted Number : {}".format(result))
        
    else:
        print("Invalid, base selectiom,Please try again\n")
        
elif ( choice == 2):
    num = int(input("Please your decimal number\n"))
    base = int(input("Please enter your preferred base\n"))


    if (2 <= base <= 36):
        result = nC.toBase(num,base)
        print("Converted Number : {}".format(result))
        
    else:
        print("Invalid, base selectiom,Please try again\n")
    
else:
    print("Invalid choice selection, Please try again\n")