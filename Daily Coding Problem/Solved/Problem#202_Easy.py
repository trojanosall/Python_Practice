# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Write a program that checks whether an integer is a palindrome.
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.


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


def palindrome_checker(num):
    if one_digit_checker(num) == True:
        return True
    else:    
        digit_list = digit_separator(num)
        reversed_digit_list = []
        for i in range(len(digit_list)-1, -1, -1):
            reversed_digit_list.append(digit_list[i])

        check_sum = 0
        for i in range(0, len(digit_list), 1):
            difference_of_list_elements_at_same_index = digit_list[i] - \
                reversed_digit_list[i]
            if difference_of_list_elements_at_same_index != 0:
                return False
                break
            else:
                check_sum += difference_of_list_elements_at_same_index
        
        if check_sum == 0:
            return True


my_number = 121
print(my_number, "is palindrome?")
print(palindrome_checker(my_number))
