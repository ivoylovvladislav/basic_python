def division(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        division_number = num_1 / num_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Division by zero'
    return round(division_number, 4)


print(division(input('Введите первое число: '), input('Введите второе число: ')))
