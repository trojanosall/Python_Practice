# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping (FULLY).

# For example, given the following rectangles:

# {
#     "top_left": (1, 4),
#     "dimensions": (3, 2) # width, height
# },
# {
#     "top_left": (-1, 3),
#     "dimensions": (2, 1)
# },
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3)
# }
# return true as the first and third rectangle overlap each other.


def get_all_valid_coordinate_of_the_rectangle(top_left_coordinate, dimension):
    all_coordinates_of_rectangle = []
    for y in range(dimension[1]+1):
        for x in range(dimension[0]+1):
            temp_new_coordinate = []
            temp_new_coordinate = [
                top_left_coordinate[0]+x, top_left_coordinate[1]-y]
            all_coordinates_of_rectangle.append(temp_new_coordinate)
    return all_coordinates_of_rectangle


def overlapping_checker(rectangles_with_all_coordinates):
    overlap_return = False

    for x in range(0, len(rectangles_with_all_coordinates), 1):
        for y in range(1, len(rectangles_with_all_coordinates), 1):
            if len(rectangles_with_all_coordinates[x]) <= len(rectangles_with_all_coordinates[y]):
                coordinate_counter = 0
                for coordinate in rectangles_with_all_coordinates[x]:
                    if coordinate in rectangles_with_all_coordinates[y]:
                        coordinate_counter += 1
                    else:
                        break
                if coordinate_counter == len(rectangles_with_all_coordinates[x]) and rectangles_with_all_coordinates[x] != rectangles_with_all_coordinates[y]:
                    overlap_return = True
                    print(f"{y}. rectanle contain {x}. rectangle.")
            else:
                coordinate_counter = 0
                for coordinate in rectangles_with_all_coordinates[y]:
                    if coordinate in rectangles_with_all_coordinates[x]:
                        coordinate_counter += 1
                    else:
                        break
                if coordinate_counter == len(rectangles_with_all_coordinates[y]) and rectangles_with_all_coordinates[x] != rectangles_with_all_coordinates[y]:
                    overlap_return = True
                    print(x + ". rectanle contain" + y + "rectangle.")
    return overlap_return


A_top_left_coordinates = [1, 4]
A_dimension = [3, 2]
A_rectangle_all_coordinates = get_all_valid_coordinate_of_the_rectangle(
    A_top_left_coordinates, A_dimension)


B_top_left_coordinates = [-1, 3]
B_dimension = [2, 1]
B_rectangle_all_coordinates = get_all_valid_coordinate_of_the_rectangle(
    B_top_left_coordinates, B_dimension)


C_top_left_coordinates = [0, 5]
C_dimension = [4, 3]
C_rectangle_all_coordinates = get_all_valid_coordinate_of_the_rectangle(
    C_top_left_coordinates, C_dimension)


rectangles_with_all_coordinates = [
    A_rectangle_all_coordinates, B_rectangle_all_coordinates, C_rectangle_all_coordinates]
rectangles_dimensions = [A_dimension, B_dimension, C_dimension]


print(" ------------------------- ")
print("OVERLAP CHECKER:")

overlapping_checker(rectangles_with_all_coordinates)
print(overlapping_checker(rectangles_with_all_coordinates))

print(" ------------------------- ")
