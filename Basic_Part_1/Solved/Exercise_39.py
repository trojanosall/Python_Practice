# Write a Python program to compute the future value of a specified principal amount, 
# rate of interest, and a number of years.


def futureValueCalculator(principalAmount, rateOfInterest, numberOfYears):
    futureValue = principalAmount * (1 + rateOfInterest / 100) ** numberOfYears
    print(futureValue)


futureValueCalculator(10000, 3.5, 7)

# Best practice

amt = 10000
int = 3.5
years = 7

future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value, 2))
