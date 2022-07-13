some_list = [9, 8, 7, 6, 4, 2, 1]
new_number = ''

while new_number != 'end':
    i = 0
    new_number = input('Введите кол-во очков (end - выход): ')

    if new_number.isdigit():
        for n in some_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        some_list.insert(i, int(new_number))
    print(some_list)
