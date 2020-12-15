# Write a Python program to sort three integers without using conditional statements and loops.

def SortingThreeNumbers(firstNumber, secondNumber, thirdNumber):
    aNumber = min(firstNumber, secondNumber, thirdNumber)
    cNumber = max(firstNumber, secondNumber, thirdNumber)
    bNumber = firstNumber + secondNumber + thirdNumber - aNumber - cNumber

    print(aNumber, bNumber, cNumber)


SortingThreeNumbers(21, 31, 1)
