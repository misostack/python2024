#!/usr/bin/env python

"""
Project: Python Tutorial 2024
Description: A zero to hero python tutorials
"""

print("Python Tutorial 2024")

# Convert a decimal number to binary format
# Convert a binary number into a decimal number


def toBinary(value):
    if value < 0:
        return None
    binary_number = ""
    integer_part = value
    while integer_part > 0:
        remainder = integer_part % 2
        integer_part = integer_part // 2
        binary_number += str(remainder)

    return binary_number


def toDecimal(binValue):
    integer_value = 0
    if binValue == "":
        return None
    exponent = len(binValue) - 1
    for c in str(binValue):
        integer_value += int(c) * 2**exponent
        exponent -= 1
    return integer_value


# convert from decimal to binary demo
aNumber = 15
aNumberBinaryFormat = toBinary(aNumber)

print(f"{aNumber} binary format is {aNumberBinaryFormat}")

# convert from binary to decimal deo
aBinaryNumber = "1111"
aDecimalFormat = toDecimal(aBinaryNumber)

print(f"{aBinaryNumber} decimal format is {aDecimalFormat}")
