# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


def substring_copy(n):
    if type(n) is not int or n < 0:
        print("Please give the n - argument - as a non-negative integer!")
    else:
        user_word = str(input("Please give me a word: "))
        if len(user_word) < 2:
            print(user_word * n)
        else:
            substring_user_word = user_word[:2]
            print(substring_user_word * n)


substring_copy(3)
