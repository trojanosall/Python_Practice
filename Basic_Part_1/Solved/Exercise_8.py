# Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red", "Green", "White", "Black"]
print("%s %s" % (color_list[0], color_list[-1]))

print((color_list[0], color_list[-1]))

####################################################

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# String Formatting

# Python uses C-style string formatting to create new, formatted strings. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", 
# special symbols like "%s" and "%d".

# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)