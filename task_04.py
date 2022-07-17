def power_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Вводить дробное число и отрицательную степень'
    return result


print(power_func(4.5, -2))
