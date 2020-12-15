# Write a Python program to determine whether variable is defined or not.

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")


# exception NameError
# Raised when a local or global name is not found. 
# This applies only to unqualified names. 
# The associated value is an error message that includes the name that could not be found.