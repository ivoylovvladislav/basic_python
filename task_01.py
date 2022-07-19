from sys import argv


def salary():
    try:
        time, rating, premium = map(float, argv[1:])
        print(f"Зарплата - {time * rating + premium}")
    except ValueError:
        print("Все данные должны быть числами")


salary()
