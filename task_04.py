some_list = input('Введите слова через пробел: ').split()

for i, value in enumerate(some_list, 1):
    print(f'{i}) {value:.10}')
