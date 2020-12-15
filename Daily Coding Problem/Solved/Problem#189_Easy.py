# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given an array of elements, return the length of the longest subarray where all its elements are distinct.
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].



given_array = [5, 1, 3, 5, 2, 3, 4, 1]

def lenght_of_longest_subarray_of_distinct_elements (given_array):
    return len(set(given_array))

print(lenght_of_longest_subarray_of_distinct_elements(given_array))
