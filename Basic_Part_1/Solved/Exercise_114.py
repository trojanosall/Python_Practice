# Write a Python program to filter the positive numbers from a list. 

num_list = [45, 55, -60, 37, -100, -105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x > 0), num_list))
print("Positive numbers are the follows:", result)