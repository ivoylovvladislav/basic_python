from functools import reduce


def multi_list(el_1, el_2):
    return el_1 * el_2


unique_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{unique_list}\nУмноженные числа\n{reduce(multi_list, unique_list)}")
