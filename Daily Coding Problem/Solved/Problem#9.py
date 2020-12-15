""" This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
 """

# elkezdett megoldás


def NonAdjacentNumberSum(MyArray):

    ListWhichContainsNumbersCombination = []
    for x in MyArray:
        ListWhichContainsNumbersCombination.append(x)

    for x in range(len(MyArray)):
        for y in range(x + 2, len(MyArray), 1):
            NewGeneratedArray = []
            NewGeneratedArray.append(MyArray[x])
            NewGeneratedArray.append(MyArray[y])
            ListWhichContainsNumbersCombination.append(NewGeneratedArray)

    for x in range(0, len(MyArray)-4, 1):
        NewGeneratedArray = []
        NewGeneratedArray.append(MyArray[x])
        for y in range(x + 2, len(MyArray), 2):
            NewGeneratedArray.append(MyArray[y])
        ListWhichContainsNumbersCombination.append(NewGeneratedArray)

    return ListWhichContainsNumbersCombination


""" print(NonAdjacentNumberSum([2, 4, 6, 2, 5, 2, 4, 6, 2, 5]))
print(len(NonAdjacentNumberSum([2, 4, 6, 2, 5]))) """


# megtalált megoldás
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:

        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return (excl if excl > incl else incl)


print(find_max_sum([2, 4, 6, 2, 5]))
