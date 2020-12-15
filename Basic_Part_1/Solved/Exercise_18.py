# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

def sum_three_number(x, y, z):
    if x == y == z:
        return (x + y + z) * 3
    else:
        return x + y + z


print(sum_three_number(1, 2, 3))
print(sum_three_number(3, 3, 3))
