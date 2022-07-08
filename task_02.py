seconds = int(input('Введите время в секундах: '))

seconds = seconds % (24 * 3600)  # остаток от деления на общее кол-во секунд в сутках
hours = seconds // 3600

seconds = seconds % 3600  # остаток от деления на общее кол-во секунд в часе
minutes = seconds // 60

seconds = seconds % 60  # остаток от деления на общее кол-во секунд в минуте

print("%02d:%02d:%02d" % (hours, minutes, seconds))
