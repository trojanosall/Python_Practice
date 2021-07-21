# Write a Python program to convert true to 1 and false to 0.

def BoolConverter(givenNumber):
    if givenNumber == True:
        return 1
    if givenNumber == False:
        return 0
    else:
        print("The given value can not be convertedas it is required.")

print(BoolConverter(True))
print(BoolConverter(False))
BoolConverter(27)
