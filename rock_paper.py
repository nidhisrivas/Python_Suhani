#!/usr/bin/python
# A Program to Create a Rock Paper Cissor Game

import random
replay = 1

while (replay == 1):
    numGames = 0
    compWins = 0
    userWins = 0

    numGames = int(input("Please Enter An Odd Number To Start The Game\n"))
    while (numGames % 2 == 0):
        print("Invalid, Please Enter an Odd number Only")
        numGames = int(input("Please Enter An Odd Number To Start The Game\n"))

    while ((userWins <= numGames // 2) and (compWins <= numGames // 2)):

        userChoice = 0
        compChoice = 0
        compChoice = random.randint(1, 3)
        userChoice = int(input("Pick Rock(1),Paper(2) or Scissors(3):"))

        while (userChoice == compChoice):
            print(
                "Darn! Do it again guys, you and computer picked the same choices, Arrh")
            compChoice = random.randint(1, 3)
            userChoice = int(input("Pick Rock(1),Paper(2) or Scissors(3):"))
            print(compChoice, userChoice)
            if (userChoice < 1 or userChoice > 3):
                print("Invalid input. Please enter 1, 2, or 3.")
                userChoice = int(
                    input("Pick Rock (1), Paper (2), or Scissors (3):\n"))

        print(compChoice, userChoice)
        # After that loop that prevents a draw, print Rock/Paper/Scissors for the user and computer by using if/elif/else statements to translate the numbers to the words
        if userChoice == 1:
            print("You picked Rock.")
        elif userChoice == 2:
            print("You picked Paper.")
        else:
            print("You picked Scissors.")

        if compChoice == 1:
            print("Computer picked Rock.")
        elif compChoice == 2:
            print("Computer picked Paper.")
        else:
            print("Computer picked Scissors.")

        # Set up an if/elif/else statement to determine who won the round and increase the number of wins for the winner
        if (userChoice == 1 and compChoice == 3) or (userChoice == 2 and compChoice == 1) or (userChoice == 3 and compChoice == 2):
            print("You won this round!")
            userWins += 1
        else:
            print("Computer won this round!")
            compWins += 1
        if userChoice == compChoice:
            print("It's a tie!")

            # Print the number of wins for the user and computer
            print("Your wins: {}".format(userWins))
            print("Computer wins: {}".format(compWins))

        # Once the loop ends because either the user or computer has won more than half the games determine who won the series and print a victory/defeat message
        if userWins > compWins:
            print("You won the series by", userWins - compWins, "games!")
        else:
            print("Computer won the series by", compWins - userWins, "games!")

        # Prompt the user if they want to play again
        playAgain = int(input("Do you want to play again? Yes = 1, No = 2 \n"))
        if playAgain == 1:
            replay = 1
        else:
            replay = 0
            print("The Game Has Ended.")
        # exit()
