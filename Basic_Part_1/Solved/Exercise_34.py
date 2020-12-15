# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


def specialSummarize(a, b):
    ReturnValue = a + b
    if ReturnValue <= 20 and ReturnValue >= 15:
        return 20
    else:
        return ReturnValue


print(specialSummarize(10, 6))
print(specialSummarize(10, 2))
print(specialSummarize(10, 12))

# Better Solution


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
