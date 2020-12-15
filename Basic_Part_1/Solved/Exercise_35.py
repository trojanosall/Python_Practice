#  Write a Python program which will return true if the two given integer values are equal 
# or their sum or difference is 5. 


def trueMaker(a, b):
    sumValue = a + b
    difer = a - b

    if a == b or sumValue == 5 or difer == 5:
        return True
    else:
        return False


print(trueMaker(7, 2))
print(trueMaker(3, 2))
print(trueMaker(2, 2))
print(trueMaker(25, 7))


# Best practice
def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False
