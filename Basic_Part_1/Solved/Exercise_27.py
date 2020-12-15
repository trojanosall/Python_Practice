# Write a Python program to concatenate all elements in a list into a string and return it.


def concatenate(list):
    concatenated_word = ""
    for element in list:
        concatenated_word = concatenated_word + str(element)
    return concatenated_word


print(concatenate([1, 5, 12, 2]))
