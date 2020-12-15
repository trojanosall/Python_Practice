# Write a Python program to compute the distance between the points(x1, y1) and (x2, y2).

import math


def distanceCalculator(pointsOfA, pointsofB):
    a = abs(pointsofB[0] - pointsOfA[0])
    b = abs(pointsofB[1] - pointsOfA[1])
    return math.sqrt(a**2+b**2)


print(distanceCalculator([4, 0], [6, 6]))
