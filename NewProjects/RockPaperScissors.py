import random
print("Welcome to my game of 'Rock, Papers, and Scissors'! This game is best out of 3\n")
computerScore = 0
playerScore = 0
 
while (computerScore <3 and playerScore<3):
    playerChoice = input("Please type either 'Rock', 'Paper', or 'Scissors'.\n")

    choiceNum = random.randint(1,3)
    computerChoice = " " 
    if (choiceNum == 1):
        computerChoice = "Rock"
    if (choiceNum == 2):
        computerChoice = "Paper"
    if (choiceNum == 3):
        computerChoice = "Scissors"
    if (playerChoice == computerChoice):
        print("It's a tie! You both chose " + playerChoice)
        print("\n")
    elif (playerChoice == "Rock" and computerChoice == "Scissors"):
        print("You win! Rock beats Scissors\n")
        playerScore += 1
    elif (playerChoice == "Paper" and computerChoice == "Rock"):
        print("You win! Paper beats Rock\n")
        playerScore += 1
    elif (playerChoice == "Scissors" and computerChoice == "Paper"):
        print("You win! Scissors beats Paper\n")
        playerScore += 1
    else:
        print("You lose! " + computerChoice + " beats " + playerChoice)
        computerScore += 1   
    print("Your score: " + str(playerScore) + " | Computer score: " + str(computerScore))
    print("\n")

print("Game Over! Final Score - You: " + str(playerScore) + " | Computer: " + str(computerScore))
print("\n")
if (playerScore > computerScore):
    print("Congratulations! You win the game!")
else:
    print("Sorry! The computer wins the game. Better luck next time!\n")
print("Thank you for playing!")


