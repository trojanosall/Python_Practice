""" This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """


def twoListMemberSumEqualNumber(list, int):
    sumTwoNumberList = []
    for x in range(len(list)):
        for y in range(x+1, len(list), 1):
            sumTwoNumber = list[x] + list[y]
            sumTwoNumberList.append(sumTwoNumber)

    for item in sumTwoNumberList:
        if item == int:
            return True


print(twoListMemberSumEqualNumber([10, 15, 3, 7], 17))
