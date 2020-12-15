# Write a Python program to add trailing and leading zeroes to a string.

str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)

# Python String ljust() Method
# Definition and Usage
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.

# Syntax
# string.ljust(length, character)

