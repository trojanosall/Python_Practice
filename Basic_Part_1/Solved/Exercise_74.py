# Write a Python program to hash a word.

soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4,
           5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

word = input("Input the word be hashed: ")

word = word.upper()

coded = word[0]

for a in word[1:len(word)]:
    i = 65-ord(a)
    coded = coded+str(soundex[i])
print()
print("The coded word is: "+coded)
print()


#####################################################################
# Python ord()
# The ord() function returns an integer representing the Unicode character.

# print(ord('5'))    # 53
# print(ord('A'))    # 65
# print(ord('$'))    # 36