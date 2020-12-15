# Write a Python program to calculate the sum over a container.


MyList = [10, 20, 30, 40]


def SumElementOfContainer(list):
    sum = 0
    for a in list:
        sum += a
    return sum


print(SumElementOfContainer(MyList))
print()
print(sum(MyList))
