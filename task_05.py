def sum_of_num():
    s = 0
    while True:
        error = False
        new_list = input('Введите числа, end - для выхода: ').split()
        for number in new_list:
            if number.lower() == 'end':
                return s
            else:
                try:
                    s += int(number)
                except ValueError:
                    error = True
        if error:
            print('Данные недопустимы')
        print(f'Сумма чисел = {s}')


print(sum_of_num())