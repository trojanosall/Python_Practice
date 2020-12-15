#  Write a Python program to add two objects if both objects are an integer type. 


def AddIf(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        print("Two aded object are not integers")


print(AddIf(10, 20))
print(AddIf("loci", "béjbi"))

# Best practice


def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b


print(add_numbers(10, 20))
print(add_numbers("loci", "béjbi"))

# 'type()' and 'isinstance()' in Python
# The variable types can be known using Python's own 'type()'. 
# The 'type()' can be used at runtime for the debugging purpose to identify the exact variable types in the program. 
# Let's look at the type of some variables in the example below.

# my_var = 12
# print(type(my_var))
# The above code will give output as 'int'. 
# Since the data type of the variable is integer where 'type()' plays a role in identifying it.

# The 'insinstance('obj','class')' of Python can be used to know whether the 'obj', which is the object is 
# the instance of the class or not. The returned output value is boolean can be one of True or False.

# my_var = "Hello"
# print(isinstance(my_var,str))
# The above code will give output as True. Since the data type of the variable is a string, 
# where 'isinstance()' plays a role in identifying it.
