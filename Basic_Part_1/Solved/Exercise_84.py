# Write a Python program to count the number occurrence of a specific character in a string.

inputChar = input("Input a character which is searched in an input string : ")

input_string = input("Input a string: ")


def OccurenceCounter(myChar, myString):
    counter = 0
    for char in myString:
        if char == myChar:
            counter += 1
    return counter


print(OccurenceCounter(inputChar, input_string))

"""BEST PRACTICE"""

print()
print()
print("BEST PRACTICE")
print()
print()

s = "The quick brown fox jumps over the lazy dog."
print()
print(s.count("q"))
print()
