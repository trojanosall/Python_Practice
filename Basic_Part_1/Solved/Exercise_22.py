# Write a Python program to count the number 4 in a given list.


def count_list_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    return count


print(count_list_4([1, 3, 4, 9, 7, 4, 6, 2, 4]))

print(count_list_4([1, 4, 6, 7, 4]))
print(count_list_4([1, 4, 6, 4, 7, 4]))
