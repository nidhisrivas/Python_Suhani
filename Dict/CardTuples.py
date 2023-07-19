#!/usr/bin/python

#A Card Tuple Program
#Date: July 17th'2023
#Author : Suhani Khare

import random

values = ('Ace','2','3','4','5','6','7','8','9','10','jack','Queen','king')
suits = ("Clubs","Hearts","Spades","Diamonds")

# Traversing Suits Tupple
for i in range(len(suits)):
    for j in range(len(values)):
        print("Printing Suit {} value {}".format(suits[i],values[j]))
    print("--------------------------\n")

randSuit = random.randint(0.3)
randVal = random.randint(0,12)


print("Random Card: {} of {}".format(values[randVal],values[randSuit]))