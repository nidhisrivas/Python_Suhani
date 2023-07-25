civic = {
  "make" : "Honda",
  "model" : "Civic",
  "year" : 2017,
  "color" : "Midnight Blue",
  "cost" : 24000
}

corvette = {
  "make" : "Chevrolet",
  "model" : "Corvette",
  "year" : 2023,
  "color" : "Red",
  "cost" : 72000
}

r8 = {
  "make" : "Audi",
  "model" : "R8",
  "year" : 2021,
  "color" : "Black",
  "cost" : 142700
}

def printCar(car):
  print("Make: {}".format(car["make"]))
  print("Model: {}".format(car["model"]))
  print("Year: {}".format(car["year"]))
  print("Color: {}".format(car["color"]))
  print("Cost: ${:,.2f}".format(car["cost"]))