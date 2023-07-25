import numpy
import math
import statistics as st 

dataset = [5, 1, 9, 12, 7, 4, 3, 8, 12, 5]
dataset.sort()
print(dataset)
meanVal = numpy.mean(dataset)

print("Mean: {:.2f}".format(meanVal))




# percentile
numWins =  [40, 56, 46, 48, 35, 46, 34, 46, 43, 37, 59, 36, 39, 60, 43, 50, 50, 58, 64, 32, 49, 39, 52, 48, 51, 50, 51, 41, 50, 31]
perc = 60
numWins.sort()
print(numWins)


# our goal is to figure out which value of wins in the dataset is greater than 60% f the rest of the data
percWins = math.floor(numpy.percentile(numWins,perc))
print("the {}th percentile of the winns is {} wins,meaning {}% of teams have less wins than that".format(perc,percWins,perc))

#30 teams in the league - 60th percentile says that 60% of the teasm have 49  wins or less
#60% of 30 is 18 teams, so 18 teams have 49 wins or less

