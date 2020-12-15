# Write a Python program to convert a byte string to a list of integers.

x = b'Abc'
print()
print(list(x))
print()

# The only thing that a computer can store is bytes.

# To store anything in a computer, you must first encode it, i.e. convert it to bytes. 
# For example:

# If you want to store music, you must first encode it using MP3, WAV, etc.
# If you want to store a picture, you must first encode it using PNG, JPEG, etc.
# If you want to store text, you must first encode it using ASCII, UTF-8, etc.
# MP3, WAV, PNG, JPEG, ASCII and UTF-8 are examples of encodings. 
# An encoding is a format to represent audio, images, text, etc in bytes.

# In Python, a byte string is just that: a sequence of bytes. 
# It isn't human-readable. 
# Under the hood, everything must be converted to a byte string 
# before it can be stored in a computer.

# On the other hand, a character string, often just called a "string", 
# is a sequence of characters. It is human-readable. 
# A character string can't be directly stored in a computer, 
# it has to be encoded first (converted into a byte string). 
# There are multiple encodings through which a character string can be 
# converted into a byte string, such as ASCII and UTF-8.
