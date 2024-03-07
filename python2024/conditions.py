import random
number = random.randint(1, 100)
is_hot = number % 3 == 0
is_cold = number % 5 == 0

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's lovely day")
print("Enjoy your day")

price_of_a_house = 1_000_000
has_good_credit = random.randint(1, 100) % 2 == 0
if has_good_credit:
    down_payment = 0.1 * price_of_a_house
else:
    down_payment = 0.2 * price_of_a_house
print(f"Down payment: ${down_payment}")

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print('Eligible for loan')

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
