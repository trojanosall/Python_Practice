# Write a Python program to get the size of an object in bytes.

import sys

str1 = "one"
str2 = "four"
str3 = "three"
str4 = "THREE"

myint = 1698
myfloat = 1896.36983

print()
print("Memory size of " + str1 + " = " + str(sys.getsizeof(str1)) + " bytes")
print("Memory size of " + str2 + " = " + str(sys.getsizeof(str2)) + " bytes")
print("Memory size of " + str3 + " = " + str(sys.getsizeof(str3)) + " bytes")
print("Memory size of " + str4 + " = " + str(sys.getsizeof(str4)) + " bytes")
print("Memory size of " + str(myint) + " = " +
      str(sys.getsizeof(myint)) + " bytes")
print("Memory size of " + str(myfloat) + " = " +
      str(sys.getsizeof(myfloat)) + " bytes")
