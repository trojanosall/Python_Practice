# Write a python program to sum of the first n positive integers.


def sumOfPositiveIntegers():
    givenNumber = int(input("Give me a number please: "))
    SumOfNumbers = 0
    for i in range(givenNumber+1):
        SumOfNumbers = SumOfNumbers + i
    return SumOfNumbers


print(sumOfPositiveIntegers())
