sales = float(input('Введите выручку - '))
expenses = float(input('Введите издержки - '))
result = sales - expenses
if result > 0:
    print(f'Ваша компания имеет прибыль {result}')
    print(f'Рентабельность {100 * (result / expenses):.1f}%')
    workers = int(input('Сколько у вас сотрудников? '))
    print(f'Если разделить прибыль, то каждый получит по {result / workers:.3f}')
elif result < 0:
    print(f'Компания получила убыток {-result}')
else:
    print(f'Пока вышли в ноль')