## A Rock Paper Scissor Game ##

Instructions:
Create the RPS.py file
Initialize replay to 1
Set up a while loop to continue while replay is 1
Initialize numGames, compWins, and userWins all to 0
Make sure that numGames is odd by using a loop that continues until numGames is odd
Prompt the user to enter an odd number of games
Once the user has entered an odd number of games, set up a loop that will continue until either the user or computer has won more than half of the games.
Initialize userChoice and compChoice to 0.
Set up a while loop that will continue as long as user and computer choices are the same. This will make sure that there isn’t a draw since it will force both to have different choices.
Generate a random number [1, 3] for the computer’s choice
Prompt the user to pick Rock (1), Paper (2), or Scissors (3)
After that loop that prevents a draw, print Rock/Paper/Scissors for the user and computer by using if/elif/else statements to translate the numbers to the words
Set up an if/elif/else statement to determine who won the round and increase the number of wins for the winner.
Print the number of wins for the user and computer
Once the loop ends because either the user or computer has won more than half the games determine who won the series and print a victory/defeat message
Prompt the user if they want to play again