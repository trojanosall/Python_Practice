# Write a Python program to calculate the hypotenuse of a right angled triangle.
import math


def hypotenuse_calculator(a, b):
    c = math.sqrt(a * a + b * b)
    return c


print(hypotenuse_calculator(3, 4))
