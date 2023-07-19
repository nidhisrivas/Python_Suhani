userProfile = {
    "First Name" : "Steven",
    "Last Name" : "Dubner",
    "Age"  : "31", "User Name" : "pypi", "Password" : "python123" }
## Setting Up Access Level

if(int(userProfile["Age"]) < 10):
    userProfile["Access Level"] = "E for Everyone"
elif(int(userProfile["Age"]) < 13):
    userProfile["Access Level"] = "10 and Up"
elif(int(userProfile["Age"]) < 18):
    userProfile["Access Level"] = "T for Teen"
else:
    userProfile["Access Level"] = "M for Mature"

username =input("Please enter your username\n")
user_input = username.lower()

if (user_input == userProfile["User Name"].lower()):
    passwd = input("Please enter your password\n")
    if(passwd == userProfile["Password"]):
        print("Welcome dear {}, {}, Your Access Level is {}".format(userProfile["First Name"],userProfile["Last Name"],userProfile["Access Level"]))

    else:
        print("Sorry, incorrect password!")
else:
    print("Sorry, Invalid Uusername")

