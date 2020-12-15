# Write a Python program to solve(x + y) * (x + y).


def solver(x, y):
    print((x + y) * (x + y))

solver(4, 3)


# Best practice
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))
