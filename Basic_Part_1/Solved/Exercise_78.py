# Write a Python program to find the available built-in modules.

import sys
import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))

####################################
# Python String join() Method
# Example
# Join all items in a tuple into a string, using a hash character as separator:

# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x) ---> John#Peter#Vicky

# Syntax
# string.join(iterable)


# Python sorted() Function
# The sorted() function returns a sorted list of the specified iterable object.

# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
# sorted(iterable, key=key, reverse=reverse)


# sys.builtin_module_names
# A tuple of strings giving the names of all modules that are compiled into this Python interpreter. (This information is not available in any other way — modules.keys() only lists the imported modules.)


# In python the textwrap module is used to format and wrap plain texts. There are some options to format the texts by adjusting the line breaks in the input paragraph.
# Module (textwrap.fill(text, width = 70, **kwargs)) −
# The fill() method is similar to the wrap method, but it does not generate a list. It generates a string. It adds the new line character after exceeding the specified width.