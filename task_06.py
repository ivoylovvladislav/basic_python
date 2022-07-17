def some_func():
    for word in input('Введите слова на английском с маленькой буквы через пробелы:\n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - только на англ и с маленькой буквы')


some_func()
