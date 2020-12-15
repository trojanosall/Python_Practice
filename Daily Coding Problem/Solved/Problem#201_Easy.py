# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
# For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
# eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5.
# The weight of the path is the sum of the entries.

# Write a program that returns the weight of the maximum weight path.

# Function for finding maximum sum


N = 3

# Function for finding maximum sum


def maxPathSum(tri, m, n):

    # loop for bottom-up calculation
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if (tri[i + 1][j] > tri[i + 1][j + 1]):
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

    # return the top element
    # which stores the maximum sum
    return tri[0][0]

# Driver program to test above function


tri = [[1, 0, 0],
       [4, 8, 0],
       [1, 5, 3]]
print(maxPathSum(tri, 2, 2))

# https://www.geeksforgeeks.org/maximum-path-sum-triangle/
