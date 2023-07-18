#!/usr/bin/python
# A Python program for newly weds to reveal how much they know each other
# Date: July 18th'2023
# Autor: "Nidhi Srivastava"

#Initilizing the names list
names =[]

#### All For Player1

#Pormpting for the players names
player1 = input("Please enter player1's name here\n")
names.append(player1)

player2 = input("Please enter player2's name here\n")
names.append(player2)

#Initialiing the tuple category tupple with 4 Q's of our choice
choice = ("Faviroute Color","Faviroute Food","Faviroute Passtime","Faviroute Sport")

#Setting up player1 and player2's ans
player1Answers = set()
player2Answers = set()

# Setting up For loop to traverse the categories list for Player1
for i in choice:
    #print(i)
    ans1 = input("Hey Dear {}, what is {},'s {}\n".format(player1,player2,i))
    player1Answers.add(ans1)

# Setting up For loop to traverse the categories list for Player2
for i in choice:
    ans2 = input("Hey Dear {}, what is your {}\n".format(player2,i))
    player2Answers.add(ans2)
    
# Setting up the intersection of both the choices obtained above using intersection of sets

matchingAnswer = player1Answers.intersection(player2Answers)

#Setting numCorr to the length of matchingAnswe
numCorr = len(matchingAnswer)
#Printing the correct ans
print("OK Dear {}, Your Number of Correct Answer is {}".format(player1,numCorr))
print("---------------------------------------------------------------------\n")


player1Answers.clear()
player2Answers.clear()

## Repeating the same for player2


#### All For Player2

# Setting up For loop to traverse the categories list for Player2

for i in choice:
    ans2= input("Hey Dear {},what is {},'s {}\n".format(player2,player1,i))
    player2Answers.add(ans2)
    # Setting up For loop to traverse the categories list for Player1
for i in choice:
    ans1 = input("Hey Dear {},what is your  {}\n".format(player1,i))
    player1Answers.add(ans1)
    
# Setting up the intersection of both the choices obtained above using intersection of sets

matchingAnswer = player2Answers.intersection(player1Answers)

#Setting numCorr to the length of matchingAnswe
numCorr = len(matchingAnswer)

#Printing the correct ans
print("Number of Correct Answer is {}".format(numCorr))
# Setting up the intersection of both the choices obtained above using intersection of sets

matchingAnswer = player1Answers.intersection(player2Answers)

#Setting numCorr to the length of matchingAnswe
print("OK Dear {}, Your Number of Correct Answer is {}".format(player2,numCorr))
print("---------------------------------------------------------------------\n")
    



