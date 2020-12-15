# Write a Python program to print to stderr.

from __future__ import print_function
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="--")

# What is stderr Python?
# Standard output and standard error (commonly abbreviated stdout and stderr) 
# are pipes that are built into every UNIX system. 
# When you print something, it goes to the stdout pipe; 
# when your program crashes and prints out debugging information (like a traceback in Python), 
# it goes to the stderr pipe.
