""" Write a Python program to get height and the width of console window. """

import os

hw = os.get_terminal_size()
print("Height:", hw[1], "Width:", hw[0])
