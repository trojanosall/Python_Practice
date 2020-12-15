# Write a Python program to calculate the sum of the digits in an integer.


def Sum_Of_Digit():
    given_number = input("Please give a number: ")
    final_result = 0
    for element in given_number:
        final_result = final_result + int(element)
    return final_result


print(Sum_Of_Digit())
