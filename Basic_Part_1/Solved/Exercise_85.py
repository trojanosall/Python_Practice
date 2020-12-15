# Write a Python program to check if a file path is a file or a directory.

import os

path = "D:\\Python\\Basic_Part_1\\Solved\\41.txt"


def fileOrDirectoryChecker(path):
    if os.path.isdir(path):
        print("\nIt is a directory")
    elif os.path.isfile(path):
        print("\nIt is a normal file")
    else:
        print("It is a special file (socket, FIFO, device file)")
    print()


fileOrDirectoryChecker(path)