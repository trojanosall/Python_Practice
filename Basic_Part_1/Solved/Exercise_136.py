# Write a Python program to find files and skip directories of a given directory.

import os

print([f for f in os.listdir(R'D:\MyRepos\Python_Practice\Basic_Part_1') if os.path.isfile(os.path.join(R'D:\MyRepos\Python_Practice\Basic_Part_1', f))])


# os.listdir(path)
# This method returns a list containing the names of the entries in the directory 
# given by path.

# os.path.isfile() 
# method in Python is used to check whether the specified path is an existing 
# regular file or not.

# os.path.join() 
# method in Python join one or more path components intelligently. 
# This method concatenates various path components with exactly one 
# directory separator (‘/’) following each non-empty part except the 
# last path component. If the last path component to be joined is 
# empty then a directory seperator (‘/’) is put at the end.
# If a path component represents an absolute path, then all previous 
# components joined are discarded and joining continues from the 
# absolute path component.