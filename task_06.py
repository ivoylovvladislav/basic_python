while True:
    days = 1
    start = float(input('Старт: '))
    stop = float(input('Финиш: '))
    if start <= 0 or stop < 0:
        print('Результат должен быть выше нуля')
    else:
        while start < stop:
            start += start * 0.1
            days += 1

        print(f'Спортсмен добьется результата за {days} дней')
        break
