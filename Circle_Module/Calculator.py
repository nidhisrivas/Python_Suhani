from CalcModule import addition, subtraction, multiplication, division, modulus

print("Welcome to the Calculator Module!\n")
first = int(input("Enter a number: "))
seconnd = int(input("Enter a number: "))

print("Choose a function:\n")
print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Modulus\n")
functionChoice = input("Please enter the number corresponding to your choice: ")

if functionChoice == "1":
    result = addition(first, seconnd)
    print("Result of Addition: {}".format(result))
    print(" ")
elif functionChoice == "2":
    result = subtraction(first, seconnd)
    print("Result of Subtraction: {}".format(result))
    print(" ")
elif functionChoice == "3":
    result = multiplication(first, seconnd)
    print("Result of Multiplication: {}".format(result))
    print(" ")
elif functionChoice == "4":
    try:
        result = division(first, seconnd)
        print("Result of Division: {}".format(result))
        print(" ")
    except ValueError as e:
        print(e)
elif functionChoice == "5":
    result = modulus(first, seconnd)
    print("Result of Modulus: {}".format(result))
    print(" ")
else:
    print("Invalid choice. Please select a valid function.\n")

print("Thank you for using the Calculator Module!")
print("Goodbye!\n")
