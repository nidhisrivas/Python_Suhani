import matplotlib.pyplot as plt

sportsNames = ['Baseball','Soccer','Football','Basketball','Tennis','Volleyball','Cricket','Badminton','Swimming','Rugby','Hockey','Figure Skating','Formula 1','Fencing','Track and Field','Wrestling']
sportsOcc= [2,33,5,20,9,19,5,7,1,3,2,1,1,1,1,1]
sportsPerc = [1.80,29.73,4.50,18.02,8.11,17.12,4.50,6.31,0.90,2.70,1.80,0.90,0.90,0.90,0.90,0.90]

print(len(sportsPerc),len(sportsNames),len(sportsOcc))
#exit()


choice = input("Please pick number 1 for bar chart \nPlease pick number 2 for Pie Chart\n")

if(choice == "1"):
    plt.bar(sportsNames,sportsOcc)
    plt.grid()
    plt.xlabel('Type of Sport')
    plt.ylabel('Number of Occurences')
    plt.show()

elif(choice == "2"):
    plt.pie(sportsPerc, labels=sportsNames)
    plt.xlabel('Type of Sport')
    plt.ylabel('Percentage of Students Who Chose That Sport')
    plt.grid()
    plt.show()


else:
    print("Invalid Choice, Please try again\n")
    

              

