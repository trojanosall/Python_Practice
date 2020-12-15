# Good morning! Here's your coding interview problem for today.

# This problem was asked by IBM.

# Given an integer, find the next permutation of it in absolute order.
# For example, given 48975, the next permutation would be 49578.

from itertools import permutations


def one_digit_checker(num):
    if (num >= 0) and (num < 10):
        return True
    else:
        return False


def digit_separator(number):
    digits_list = []
    if one_digit_checker(number):
        digits_list.append(number)
    else:
        temp_number = number
        while one_digit_checker(temp_number) == False:
            last_digit = temp_number % 10
            digits_list.append(int(last_digit))
            temp_number = temp_number - last_digit
            temp_number = temp_number / 10
            if one_digit_checker(temp_number) == True:
                digits_list.append(int(temp_number))
    return digits_list


def next_permutation_finder(my_number):
    my_digit_list = digit_separator(my_number)
    my_perm = permutations(my_digit_list)
    my_perm_list = list(my_perm)
    perm_num_list = []
    for one_perm in my_perm_list:
        temp_sum = 0
        for k in range(0, len(one_perm), 1):
            if one_perm[k] == 0:
                break
            else:
                temp_sum += one_perm[k] * 10**(len(one_perm)-(k+1))
        perm_num_list.append(temp_sum)
    differences = []
    temp_diff = 0
    for perm_num in perm_num_list:
        if perm_num > my_number:
            temp_diff = perm_num - my_number
            differences.append(temp_diff)
    min_diff = min(differences)
    next_permutation = my_number + min_diff
    return next_permutation


my_number = 48975

print(next_permutation_finder(my_number))
