number = int(input('Введите число: '))
max_num = 0
temp_num = number

while temp_num > 0:
    one_num = temp_num % 10
    if one_num > max_num:
        max_num = one_num
        if max_num == 9:
            break
    temp_num = temp_num // 10


print(f'Наибольшая цифра в числе {number} равна {max_num}')
