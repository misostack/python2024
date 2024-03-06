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
