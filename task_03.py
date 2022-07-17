def new_func(num_1, num_2, num_3):
    try:
        new_list = list(map(float, [num_1, num_2, num_3]))
        new_list.remove(min(new_list))
        return sum(new_list)
    except (TypeError, ValueError):
        return 'Вводите только числа'


print(new_func(input('Первое число - '), input( 'Второе число - '), input('Третье число - ')))