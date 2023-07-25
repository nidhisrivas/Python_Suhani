def detIntRate(credScore):
  if 780 < credScore <= 850:
    interestRate = 5.18
  elif credScore > 660:
    interestRate = 6.4
  elif credScore > 600:
    interestRate = 8.86
  elif credScore > 500:
    interestRate = 11.53
  else:
    interestRate = 14.08
  interestRate /= 100
  # since it's monthly percentages we need, divide that by 12
  interestRate /= 12
  return interestRate


def calcMonthlyPayment(interest, years, principal):
  numerator = interest * ((1 + interest) ** (years * 12))
  denominator = ((1 + interest) ** (years * 12)) - 1
  amount = principal * numerator / denominator
  return amount