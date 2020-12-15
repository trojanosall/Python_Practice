
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

# For example, given the following rectangles:

# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3)  # width, height
# }
# and

# {
#     "top_left": (0, 5),
#     "dimensions" (4, 3)  # width, height
# }
# return 6.


def Give_Back_Rectangle_coordinates(top_left_coordinates, dimension):
    width = dimension[0]
    height = dimension[1]
    top_left = top_left_coordinates
    top_right = [top_left[0]+width, top_left[1]]
    bottom_left = [top_left[0], top_left[1]-height]
    bottom_right = [top_right[0], bottom_left[1]]
    rectangle_coordinates = [top_left, top_right, bottom_left, bottom_right]
    return rectangle_coordinates


def IntersectionCalculator(A_Rectangle_Coordinates, B_Rectangle_Coordinates):
    C_Top_Left_Coordinate = [max(A_Rectangle_Coordinates[0][0], B_Rectangle_Coordinates[0][0]), min(
        A_Rectangle_Coordinates[0][1], B_Rectangle_Coordinates[0][1])]

    C_Top_Right_Coordinate = [min(A_Rectangle_Coordinates[1][0], B_Rectangle_Coordinates[1][0]), min(
        A_Rectangle_Coordinates[1][1], B_Rectangle_Coordinates[1][1])]

    C_Bottom_Left_Coordinate = [max(A_Rectangle_Coordinates[2][0], B_Rectangle_Coordinates[2][0]), max(
        A_Rectangle_Coordinates[2][1], B_Rectangle_Coordinates[2][1])]

    C_Width = C_Top_Right_Coordinate[0] - C_Top_Left_Coordinate[0]

    C_Height = C_Top_Left_Coordinate[1] - C_Bottom_Left_Coordinate[1]

    Intersection = C_Width * C_Height

    if Intersection <= 0:
        return 0
    else:
        return Intersection


A_top_left_coordinates = [-4, -1]
A_dimension = [3, 3]

A_Rectangle_Coordinate = Give_Back_Rectangle_coordinates(
    A_top_left_coordinates, A_dimension)
print(A_Rectangle_Coordinate)


B_top_left_coordinates = [-3, -3]
B_dimension = [3, 3]

B_Rectangle_Coordinate = Give_Back_Rectangle_coordinates(
    B_top_left_coordinates, B_dimension)
print(B_Rectangle_Coordinate)

print(IntersectionCalculator(A_Rectangle_Coordinate, B_Rectangle_Coordinate))
