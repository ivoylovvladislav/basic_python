from itertools import count, cycle

print('Программа генерирует целые числа. Нажмите enter'
      ' или выход из программы - "end"')
for i in count(int(input('Введите первое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'end':
        break

print(
    'Программа повторяет элементы списка. Нажмиет enter'
    ' или выход из программы - "end"')
unique_list = input('Введите элементы через пробелы: ').split()
iter = cycle(unique_list)
quit = None

while quit != 'end':
    print(next(iter), end='')
    quit = input()
