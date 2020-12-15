# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 
# return double the absolute difference.

given_number = int(input("Please give me a number: "))
the_number = 17

if given_number >= the_number:
    print((given_number - the_number) * 2)
else:
    print(the_number - given_number)


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(22))
print(difference(14))
