# Write a Python program to create a bytearray from a list.

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()

# Python supports a range of types to store sequences. 
# There are six sequence types: strings, byte sequences (bytes objects), 
# byte arrays (bytearray objects), lists, tuples, and range objects.

# bytearray() function :
# Return a new array of bytes. The bytearray type is a mutable sequence of integers 
# in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, 
# described in Mutable Sequence Types, as well as most methods that the bytes type has, 
# see Bytes and Byte Array Methods.