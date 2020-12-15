# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an array and a number k that's smaller than the length of the array, 
# rotate the array to the right k elements in-place.

nums = [1,2,3,4,5,6,7]
k = 3

def rotate_array(array_of_numbers, l):
    for x in range(l):
        array_of_numbers.insert(0, array_of_numbers.pop(len(array_of_numbers)-1))
    
    return array_of_numbers

print(rotate_array(nums, k))

