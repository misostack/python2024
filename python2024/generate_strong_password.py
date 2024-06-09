#!/usr/bin/env python
import random


def get_alphabet():
    alphabet = ""
    c = ord("a")
    while c <= ord("z"):
        alphabet += chr(c)
        c += 1

    return list(alphabet)


def get_symbols():
    return list("!@#$%^&*()_+:\"?><~+-=_")


def get_digits():
    digits = []
    i = 0
    while i <= 9:
        digits.append(i)
        i += 1
    return digits


def random_item(items):
    l = len(items)
    idx = random.randint(0, l - 1)
    item = items[idx]
    return item


def generate_symbol():
    symbols = get_symbols()
    # return random_item(symbols)
    return random.choice(symbols)


def generate_letter():
    letters = get_alphabet()
    # return random_item(letters)
    return random.choice(letters)


def generate_digit():
    digits = get_digits()
    # return random_item(digits)
    return random.choice(digits)


def generate_character(ctype):
    if ctype == "letter":
        letter = generate_letter()
        return letter if random.randint(0, 1) % 2 == 0 else str(letter).upper()
    elif ctype == "symbol":
        return generate_symbol()
    elif ctype == "digit":
        return str(generate_digit())
    return ""


def generate_strong_password(number_of_letters, number_of_symbols, number_of_digits):
    password = []
    for c in range(1, number_of_letters + 1):
        password.append(generate_character("letter"))
    for c in range(1, number_of_symbols + 1):
        password.append(generate_character("symbol"))
    for c in range(1, number_of_digits + 1):
        password.append(generate_character("digit"))
    random.shuffle(password)
    output = ""
    for c in password:
        output += c
    return output


if __name__ == "__main__":
    password = generate_strong_password(6, 2, 2)
    print(password)
