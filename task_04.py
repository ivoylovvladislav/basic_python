from random import randint

new_list = [randint(-10, 10) for _ in range(20)]
unique_list = [el for el in new_list if new_list.count(el) == 1]
print(f"Исходный список\n{new_list}\nСписок с уникальными элементами\n{unique_list}")
