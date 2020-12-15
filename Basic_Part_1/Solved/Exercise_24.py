# Write a Python program to test whether a passed letter is a vowel or not.


def vowel_checker(letter):
    all_vowel = "aeiouAEIOU"
    return letter in all_vowel


print(vowel_checker("a"))
print(vowel_checker("E"))
print(vowel_checker("X"))
