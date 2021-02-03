# Write a Python program to input two integers in a single line.

print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# def myfunc(n):
#       return len(n)

# x = map(myfunc, ('apple', 'banana', 'cherry'))
#convert the map into a list, for readability:
# print(list(x))
# [5, 6, 6]

# The split() method splits a string into a list.

# You can specify the separator, default separator is any whitespace.
