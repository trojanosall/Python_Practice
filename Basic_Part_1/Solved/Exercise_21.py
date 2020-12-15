# Write a Python program to find whether a given number (accept from the user) is even or odd, 
# print out an appropriate message to the user.

user_number = int(input("Please give me a number: "))

modulus = user_number % 2

if modulus > 0:
    print("The given number is odd.")
else:
    print("The given number is eleven.")
