# Write a Python program to get an absolute file path.

import os


def abs_file_path(path_file_name):
    return os.path.abspath(path_file_name)


print(abs_file_path("Exercise_63.py"))
