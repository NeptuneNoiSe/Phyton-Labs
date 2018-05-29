# Лабораторная работа №7 Вариант 2.
from math import tan, acosh
print('Здравствуйте')

# Ввод значений
a = int(input('Введите a:'))
xMin = int(input('Введите минимальное значение x: '))
xMax = int(input('Введите максимальное значение x: '))
stepCount = int(input('Введите количество шагов для вычисления функции: '))
if stepCount <= 0:
    print ('Ошибка: Количество шагов не может быть меньше или равно нулю')
    exit()

# Массив значений Функции
massiveStorage = {'G':[], 'F':[], 'Y':[]}

def calc(a, x):
    try:
       g=(7 * ((-15 * a**2) + (22 * a * x) + (5 * x**2))) / ((4 * a**2) + (7 * a * x) + (3 * x**2))
       massiveStorage['G'].append(g)
    except ZeroDivisionError:
        pass

    try:
       f = -tan((4 * a**2) - (3 * a * x) - (7 * x**2))
       massiveStorage['F'].append(f)
    except ValueError:
        pass

    try:
       y = acosh((-7 * a**2) + (20 * a * x) + (3 * x**2) + 1)
       massiveStorage['Y'].append(y)
    except ValueError:
         pass

# Цикл
count = 0
while count < stepCount:
    x = xMin + count
    if xMin < xMax:
        calc(a, x)
        count +=1
    else:
        print('Ошибка: Максимальное значение меньше или равно минимальному')
        break

# Запись лога
with open('log.txt', 'w') as file:
    for key, value in massiveStorage.items():
        file.write('{} = {}\n' .format(key, value))

# Очистка массива
massiveStorage = {}

# Чтение лога
with open('log.txt', 'r') as file:
    for i in file.readlines():
        key, value = i.strip().split('=')
        print(key, '=', value)
