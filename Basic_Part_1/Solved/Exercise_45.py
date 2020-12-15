# Write a python program to call an external command in Python.

from subprocess import call

call(["dir", "-l"], shell=True)

