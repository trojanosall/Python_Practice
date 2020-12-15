# Write a Python program to convert the distance(in feet) to inches, yards, and miles.


def big_converter():
    given_number = float(input("Please give me the lenght in feet: "))
    inch = given_number * 12
    yard = given_number / 3
    mile = given_number / 5280
    print("The distance in inches is %i inches." % inch)
    print("The distance in inches is %.2f yard." % yard)
    print("The distance in inches is %.2f mile." % mile)


big_converter()
