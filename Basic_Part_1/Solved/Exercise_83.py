# Write a Python program to test whether all numbers
# of a list is greater than a certain number.

a = int(input("Input an integer : "))

input_string = input("Enter a list element separated by space: ")
Mylist = input_string.split()
MyNumList = [int(x) for x in Mylist]


def GreaterTester(inputNumber, nums):
    checkNum = 0
    for num in nums:
        if inputNumber < num:
            checkNum += 1
    if checkNum == len(nums):
        print("All numbers of a list is greater than a certain number.")
    else:
        print("Not all numbers of a list is greater than a certain number.")


GreaterTester(a, MyNumList)

"""BEST PRACTICE"""

print("BEST PRACTICE")
print()
print()

num = [2, 3, 4]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()

# Python all() Function
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.
# mylist = [True, True, True]
# x = all(mylist)
