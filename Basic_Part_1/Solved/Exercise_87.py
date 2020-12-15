# Write a Python program to get the size of a file.

import os


def File_Size(fileName):
    file_size = os.path.getsize(fileName)
    return file_size


print("File size in bytes of a plain file: ",
      File_Size("D:\\Python\\Basic_Part_1\\Solved\\Exercise_36.py"), "bytes")
