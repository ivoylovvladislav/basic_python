def person_info(**kwargs):
    return ' '.join(kwargs.values())


print(person_info(name=input('Введите имя: '), surname=input('Введите фамилию: '),
                  birth=input('Год рождения: '), city=input('Ваш город: '),
                  email=input('Ваш email: '), phone=input('Номер телефона: ')))
