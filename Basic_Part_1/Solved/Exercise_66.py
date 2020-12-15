# Write a Python program to calculate body mass index.


def BMI_Calculator():
    weight = float(input("Your weight: "))
    height = float(input("Your height: "))
    BMI = weight / (height * height)
    print("Your BMI is %s." % BMI)


BMI_Calculator()
