import cars
import financing as fin


print("1 - ")
# moduleName.functionName(moduleName.dictionaryName)
cars.printCar(cars.civic)
print("-" * 20)
print("2 - ")
cars.printCar(cars.corvette)
print("-" * 20)
print("3 - ")
cars.printCar(cars.r8)
print("-" * 20)
choice = int(input("Choose (Enter 1, 2, or 3): "))
if 1 <= choice <= 3:
  if choice == 1:
    car = cars.civic
  elif choice == 2:
    car = cars.corvette
  else:
    car = cars.r8
  # access the user choice's car cost
  principalAmount = car["cost"]
  downPayment = float(input("Enter amount for downpayment: $"))
  principalAmount -= downPayment
  years = float(input("Enter number of years for loan: "))
  creditScore = int(input("Enter your credit score: "))
  interestRate = fin.detIntRate(creditScore)
  # get the monthly payment by passing in information to the calcMonthlyPayment function from our fincancing module
  monthlyPayment = fin.calcMonthlyPayment(interestRate, years, principalAmount)
  # this totalCost is the amount of the LOAN
  totalCost = monthlyPayment * 12 * years
  print("Monthly Payment: ${:,.2f}".format(monthlyPayment))
  print("Total Cost of Loan: ${:,.2f}".format(totalCost))
  print("-" * 20)
  # this is how much total money we actually paid for the car
  totalCarCost = totalCost + downPayment
  print("After {} years, you will have paid ${:,.2f} for the {}, which is ${:,.2f} more than it originally costed.".format(years, totalCarCost, car["model"], totalCarCost - car["cost"]))
else:
  print("Please leave, you can't even follow directions.")
