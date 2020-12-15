# Given variables x=30 and y=20, write a Python program to print t "30+20=50"

x = int(input("Input an integer as x: "))
y = int(input("Input an integer as y: "))


def Cumulator(a_num, b_num):
    print(a_num, "+", b_num, "=", (a_num + b_num))


Cumulator(x, y)

x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()

# String Formatting

# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
