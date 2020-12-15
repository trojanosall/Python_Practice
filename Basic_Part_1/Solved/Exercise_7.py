# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))

# Python str.rsplit(sep=None, maxsplit=-1) function:

# The function returns a list of the words of a given string using a separator as the delimiter string.

# If maxsplit is given, the list will have at most maxsplit+1 elements.
# If maxsplit is not specified or -1, then there is no limit on the number of splits.
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
# The sep argument may consist of multiple characters.
# Splitting an empty string with a specified separator returns [''].


# Both str() and repr() methods in python are used for string representation of a string. 
# Though they both seem to serve the same puppose, there is a little difference between them.

# Key differences
# str()   Make object readable    Generate output to end user
# repr()  Required code that reproduces object    Generate output for developer