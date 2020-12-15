# Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# https://www.w3schools.com/python/python_datetime.asp
