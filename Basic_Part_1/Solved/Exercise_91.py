# Write a Python program to swap two variables.


def swap_Func(a, b):
    temp_a = b
    b = a
    a = temp_a
    print(a, b)


swap_Func(5, 10)
