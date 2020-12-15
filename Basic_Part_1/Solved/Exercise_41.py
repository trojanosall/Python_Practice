# Write a Python program to check whether a file exists.

import os.path

# open("41.txt", "w")

print(os.path.isfile("41.txt"))

# os.path.isfile(path)
# Return True if path is an existing regular file. 
# This follows symbolic links, so both islink() and isfile() can be true for the same path.
