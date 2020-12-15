# Write a Python program to input a number, if it is not a number generate an error message

try:
  num = float(input("Input a number: "))
  print("It is correct. ", num, "is a number")
except:
  print("It is NOT correct. The given number is NOT a number.")

# BEST PRACTICE:
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()