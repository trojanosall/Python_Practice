""" This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.

You can modify the input array in-place.
 """


def theLowestPositiveIntegerFinder(myArray):
    mySelectedArray = []
    for x in myArray:
        if (x >= 0):
            mySelectedArray.append(x)
    lowestMemberOfMySelectedArray = min(mySelectedArray)
    for y in range(1, len(mySelectedArray)+1, 1):
        resultNumber = lowestMemberOfMySelectedArray + y
        if resultNumber not in mySelectedArray:
            return resultNumber


print(theLowestPositiveIntegerFinder([3, 4, -1, 1]))
