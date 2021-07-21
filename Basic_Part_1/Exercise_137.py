# Write a Python program to extract single key-value pair of a dictionary in variables.

d = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = d.items()

print(x)

for item in x:
    for elem in item:
        print(elem)
