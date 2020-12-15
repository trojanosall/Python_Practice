import traceback

# Write a Python program to print the current call stack.


print()


def f1(): return abc()


def abc(): traceback.print_stack()


f1()
print()

# A traceback is a report containing the function calls made in your code at a specific point. 
# Tracebacks are known by many names, including stack trace, stack traceback, backtrace, 
# and maybe others. In Python, the term used is traceback.
# When your program results in an exception, Python will print the current traceback to help you 
# know what went wrong. 
