# Write a Python program to check if a string is numeric.


def numeric_checker(my_string):
    if my_string.isdigit():
        print(my_string + " is numeric.")
    else:
        print(my_string + " is NOT numeric.")


numeric_checker("12364")
numeric_checker("1236sunnn")

str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

# Python String isdigit() Method

# Check if all the characters in the text are digits.
