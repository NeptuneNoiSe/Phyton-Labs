# Лабораторная работа №4 Вариант 2.
from math import tan, acosh
print('Здравствуйте')

# Ввод значений
a = int(input('Введите a:'))
xMax = int(input('Введите максимальное значение x: '))
xMin = int(input('Введите минимальное значение x: '))
stepCount = int(input('Введите количество шагов для вычисления функции: '))
if stepCount <= 0:
    print ('Ошибка: Количество шагов не может быть меньше или равно нулю')
    exit()

#Выбор Функции
func = int(input('Выберите Функцию для вычиления: '
                 '\n   Для расчета функции G: Введите 1'
                 '\n   Для расчета функции F: Введите 2'
                 '\n   Для расчета функции Y: Введите 3'
                 '\nНомер Функции: '))
if (func > 3) or (func < 1):
    print('Ошибка: Такой функции не существует')

# Функции
X = []
A = []
R = []

def calc(a, x):
   if func == 1:
    try:
       X.append(x)
       A.append(a)
       R.append((7 * ((-15 * a**2) + (22 * a * x) + (5 * x**2))) / ((4 * a**2) + (7 * a * x) + (3 * x**2)))
    except ZeroDivisionError:
          print ('Ошибка: Деление на Ноль')

   elif func == 2:
    F = -tan((4 * a**2) - (3 * a * x) - (7 * x**2))
    X.append(x)
    A.append(a)
    R.append(F)

   elif func == 3:
    try:
      X.append(x)
      A.append(a)
      R.append(acosh((-7 * a**2) + (20 * a * x) + (3 * x**2) + 1))
    except ValueError:
      print('Ошибка: Значение выходит за область определения функции')

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

# Формирования таблицы
print('X    A  Результат')
for table in zip (X, A, R):
    print('{0:.0f}   {1:.0f}  {2:.3f}'.format(*table))

# Нахождение Максимального и Минимального результата
print('Максимальнй результат: ' + str(max(R)))
print('Минимальный результат: ' + str(min(R)))
