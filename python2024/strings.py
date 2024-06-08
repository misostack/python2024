#!/usr/bin/env python
a_string = "A python's string"
another_string = 'Another "python" string'
email_content = """
This is an email content of python course for beginner
"""

alphabet = "abcdefg"
print(alphabet[0] == "a")  # a
print(alphabet[-1] == "g")  # g
print(alphabet[0:2] == "ab")  # ab
print(alphabet[1:] == "bcdefg")  # bcdefg
print(alphabet[0:-2] == "abcde")  # abcde
print(alphabet[::] == "abcdefg")  # abcdefg

another_alphabet = alphabet[:]
print(another_alphabet == "abcdefg")

# format string
first_name = 'John'
last_name = 'Smith'
message = f'{first_name} [{last_name}] is a coder'
print(message, len(first_name), len(last_name), message.upper())
print(f'Index of the 1st character of message is {message.find("i")}')
message = message.replace('John', 'Lee')
print(message)

print('Lee' in message, 'lee' in message)
print('tada d'.title(), 'tada d'.upper(), 'tada d'.lower())

# string interpolation
name = "Python2024"
target = "beginners"
print(f"This is {name} course for {target}\n")

# string format
print("This is {} course for {}\n".format(name, target))

# % Operator
print("This is %s course for %s" % (name, target))

# We can also use expressions inside the curly braces
x, y = 1, 2
print(f"{x} + {y} = {x+y}")

# Raw string
print(r"C:\workplace\nestjs")

# Let's play with string
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"{alphabet[0]}")
print(f"{alphabet[-1]}")
print(alphabet.find("M"))

# replace
alphabet = alphabet.replace("m", "M")
print(alphabet)

# slicing
print(alphabet[0:5])

# split
print("a,b,c,d,e,f".split(","))

# strip
print(len(" a ".strip()))
print(len("    a     ".strip()))

# upper
print(alphabet[1].upper())
