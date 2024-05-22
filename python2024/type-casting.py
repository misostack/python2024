#!/usr/bin/env python
from datetime import datetime


birth_year = input('Birth year: ')
print(type(birth_year))
# we need to convert input value (string) to number(integer)
today = datetime.now()
print(type(today))
age = today.year - int(birth_year)
print(type(age))
print(age)
