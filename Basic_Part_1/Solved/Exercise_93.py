# Write a Python program to get the identity of an object.

MyObject = 1
print(id(MyObject))

obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)
print()

# “Objects are Python’s abstraction for data. 
# All data in a Python program is represented by objects or by relations between objects.”

# “Every object has an identity, a type and a value.”

# “An object’s identity never changes once it has been created; 
# you may think of it as the object’s address in memory.”

# “Theid() function returns an integer representing its [the object’s] identity.”

# “The type() function returns an object’s type (which is an object itself). 
# Like its identity, an object’s type is also unchangeable.”

# “It is possible in some cases to change an object’s type, 
# under certain controlled conditions. 
# It generally isn’t a good idea though, since it can lead to some very strange behaviour 
# if it is handled incorrectly.”

# “The value of some objects can change. 
# Objects whose value can change are said to be mutable; 
# objects whose value is unchangeable once they are created are called immutable.”

# “An object’s mutability is determined by its type; 
# for instance, numbers, strings and tuples are immutable, 
# while dictionaries and lists are mutable.”
