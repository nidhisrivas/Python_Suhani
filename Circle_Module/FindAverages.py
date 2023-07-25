#!/usr/bin/python

import random
from Datasets import myTupple as mT 
from Datasets import myList1 as mL

sum = 0
choice = 0
while( choice < 1 or choice > 3):
  choice = int(input("Choose: \n1 - Use My List\n2 -User Random List\n3 - Enter Your Own List\n"))
  if choice ==1:
      for num in mL:
          sum += num
          average = sum / len(mL)
      print(mL)
      print("Average: {:.2f}".format(average))
  elif choice ==2:
     size = int(input("Enter size of the list: "))
     min = int(input("Enter minimum your random numbers can be:\n"))
     max = int(input("Enter maximum your randon numbers can be:\n"))
     randList = []

     for x in range(size):
         num = random.randint(min,max)
         randList.append(num)

     for num in randList:
         sum += num
     average = sum / size
     print(randList)
     print("Average: {:.2f}".format(average))
     
  elif choice == 3:
      size = int(input("Enter the size of the list: "))
      userList = []
      for x in range(size):
          num = int(input("Enter a value: \n"))
          userList.append(num)
      for num in userList:
          sum += num
          average = sum / size
      print(userList)
      print("Average : {:.2f}".format(average))
          
  else:
      print("Invalid Selection...try again!\n")
      print("Good Bye")
          
      
      
         
        
               