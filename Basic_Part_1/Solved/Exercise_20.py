# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copies_string(str, int):
    result = ""
    for i in range(int):
        result = result + str
    return result


print(copies_string('abc', 2))
print(copies_string('.py', 3))
