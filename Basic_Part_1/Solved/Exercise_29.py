# Write a Python program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}


def ListComparetor(A_list, B_list):
    return list(set(A_list) - set(B_list))


print(ListComparetor(["White", "Black", "Red"], ["Red", "Green"]))