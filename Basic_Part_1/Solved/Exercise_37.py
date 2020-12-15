#  Write a Python program to display your details like name, age, address in three different lines. 


def detailDisplay(name, age, address):
    print(name)
    print(age)
    print(address)


detailDisplay("Lajos Lorant", "35", "2030, Erd, Titkos u. 17")


# Best practice

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


# personal_details()

# Python String format() Method

# Definition and Usage
# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# The format() method returns the formatted string.

# Syntax
# string.format(value1, value2...)

# https://www.w3schools.com/python/ref_string_format.asp

