# Write a Python program to get the current value of the recursion limit.

import sys

print()
print("Current value of the recusrion limit: ")
print(sys.getrecursionlimit())
print()


# This limit prevents any program from getting into infinite recursion, 
# Otherwise infinite recursion will lead to overflow of the C stack and crash the Python.