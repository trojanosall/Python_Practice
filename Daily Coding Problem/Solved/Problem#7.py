""" This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
 """

abcDictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}


def theCounter(msg):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    MessageChecker = 1
    for element in msg:
        if element not in str(numbers):
            MessageChecker = 0
            break
    if MessageChecker == 0:
        print("Uncorrect Message")
    else:
        if not msg:
            return 1
        elif int(msg[:2]) > 9 and int(msg[:2]) < 27:
            return theCounter(msg[1:]) + theCounter(msg[2:])
        else:
            return theCounter(msg[1:])


print(theCounter("102"))
