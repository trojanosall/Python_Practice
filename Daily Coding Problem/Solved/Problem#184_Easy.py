# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given n numbers, find the greatest common denominator between them.

# For example, given the numbers[42, 56, 14], return 14.

Numbers = [42, 56, 14]


def greatest_common_denominator_finder(numbers):
    possible_greatest_common_denominator = []
    for x in numbers:
        for y in numbers:
            if y % x != 0:
                break
    possible_greatest_common_denominator.append(x)
    print("Greatest common denominator between the given list",
          max(possible_greatest_common_denominator))


def greatest_common_denominator_finder_2(numbers):
    min_element_of_given_list = min(numbers)

    for y in numbers:
        if y % min_element_of_given_list != 0:
            break
    greatest_common_denominator = min_element_of_given_list

    print("Greatest common denominator between the given list",
          greatest_common_denominator)


greatest_common_denominator_finder(Numbers)
greatest_common_denominator_finder_2(Numbers)
