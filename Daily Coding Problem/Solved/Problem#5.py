""" This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


Implement car and cdr.
 """


def cons(a, b):
    myList = []
    myList.append(a)
    myList.append(b)
    return myList


def car(myList):
    return myList[0]


def cdr(myList):
    return myList[1]


print(cons("kuty", "kurugy"))

print(car(cons("kuty", "kurugy")))

print(cdr(cons("kuty", "kurugy")))
