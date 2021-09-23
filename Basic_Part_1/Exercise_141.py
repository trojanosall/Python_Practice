# Write a python program to convert decimal to hexadecimal.
# Sample decimal number: 30, 4
# Expected output: 1e, 04

number1 = 30
number2 = 4

def ConverterDecimalToHexa(decimalNumber):
    return hex(decimalNumber)

print(ConverterDecimalToHexa(number1))
print(ConverterDecimalToHexa(number2))

x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))