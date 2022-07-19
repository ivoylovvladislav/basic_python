from itertools import count
from math import factorial


def factorial_func():
    for el in count(1):
        yield factorial(el)


x = 0
for i in factorial_func():
    if x == 15:
        break
    else:
        x += 1
        print(f"Факториал {x} = {i}")
