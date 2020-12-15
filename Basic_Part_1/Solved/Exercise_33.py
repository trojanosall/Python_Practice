# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def three_given_integer_manipulator(first_num, second_num, third_num):
    if first_num == second_num or first_num == third_num or second_num == third_num:
        return 0
    else:
        return first_num + second_num + third_num


print(three_given_integer_manipulator(1, 2, 3))
print(three_given_integer_manipulator(1, 2, 1))
print(three_given_integer_manipulator(1, 1, 2))
print(three_given_integer_manipulator(1, 2, 2))
