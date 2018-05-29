# Лабораторная работа №7 Вариант 2.
from math import tan, acosh
import pickle
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
class ResultStorage:
   massiveG = []
   massiveF = []
   massiveY = []

   def add_G(self, result):
        self.massiveG.append(result)

   def add_F(self, result):
        self.massiveF.append(result)

   def add_Y(self, result):
        self.massiveY.append(result)

   def clear(self):
      self.massiveG = []
      self.massiveF = []
      self.massiveY = []

   def Result (self):
       print('Массив значений G: ' + str(self.massiveG))
       print('Массив значений F: ' + str(self.massiveF))
       print('Массив значений Y: ' + str(self.massiveY))

resultstorage = ResultStorage ()

def calc(a, x):
    try:
       resultstorage.add_G((7 * ((-15 * a**2) + (22 * a * x) + (5 * x**2))) / ((4 * a**2) + (7 * a * x) + (3 * x**2)))
    except ZeroDivisionError:
        pass

    try:
       resultstorage.add_F (-tan((4 * a**2) - (3 * a * x) - (7 * x**2)))
    except ValueError:
        pass

    try:
       resultstorage.add_Y ((acosh((-7 * a**2) + (20 * a * x) + (3 * x**2) + 1)))
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

# Модуль Picle Запись и чтение файла

print ('Создание и запись массива в файл')
f = open(r'massive.txt', 'wb')
pickle.dump(resultstorage.massiveG, f)
pickle.dump(resultstorage.massiveF, f)
pickle.dump(resultstorage.massiveY, f)
f.close()

print ('Очистка структур массива')
resultstorage.clear()

print ('Открытие файла масcива структур')
f = open(r'massive.txt', 'rb')
resultstorage.massiveG = pickle.load(f)
resultstorage.massiveF = pickle.load(f)
resultstorage.massiveY = pickle.load(f)

print ('Результат:')
print(resultstorage.Result())
