# Write a Python program to extract the filename from a given path
import os


def file_name_identifier(path):
    print(os.path.basename(path))


file_name_identifier(R"D:\Python\Basic_Part_1\Solved\Exercise_102.py")