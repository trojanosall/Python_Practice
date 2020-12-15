# Write a Python program to calculate midpoints of a line

print("Calculate the midpoints of a line")

x1 = float(input("Give the x parameter of star point of the line (x1): "))
y1 = float(input("Give the y parameter of star point of the line (y1): "))

x2 = float(input("Give the x parameter of end point of the line (x2): "))
y2 = float(input("Give the y parameter of end point of the line (y1): "))

x_midpoint = (x1 + x2) / 2
y_midpoint = (y1 + y2) / 2

print("The midpoints of the line are the followings: " +
      str(int(x_midpoint)) + " and " + str(int(y_midpoint)))
