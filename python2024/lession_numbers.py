#!/usr/bin/env python
import math

division = 10/3;
division_string = str(division)
parts = division_string.split('.')
print(parts)
print(division, len(str(division)))
x = 10
print(x**2)
print(x+3)
x += 2
print(x)

# operator precedence
a = 2 + 2 * 2**3
print(a)

# math function
x = 2.9123
print(round(2.9, 2))
print(abs(-2))
print(math.ceil(x))
print(math.floor(x))