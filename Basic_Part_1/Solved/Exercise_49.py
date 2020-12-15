# Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir(
    R'D:\Python\Basic_Part_1') if isfile(join(R'D:\Python\Basic_Part_1', f))]

print(files_list)
