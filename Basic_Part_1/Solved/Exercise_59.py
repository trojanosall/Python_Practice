# Write a Python program to convert height(in feet and inches) to centimeters.


def footToCentimeterConverter():
    given_number_in_foot = float(input("Give me a parameter in foot: "))
    given_number_in_cm = given_number_in_foot * 30.48
    return given_number_in_cm


print(footToCentimeterConverter())
