# Лабораторная работа №8 Вариант 2.
import numpy as np
import time
print('Здравствуйте')
# Ввод данных
c_x = float(input('Введите координату Х для центра окружности: '))
c_y = float(input('Введите координату Y для центра окружности: '))
radius = float(input('Введите радиус окружности: '))
point = int(input('Введите количество точек: '))
times = []
# Расчеты
def calc():
    for key in x:
        key_x = (key - c_x)**2
        r_x.append(key_x)
    for key in y:
        key_y = (key - c_y)**2
        r_y.append(key_y)
    result = list(map(lambda a, b: a + b, r_x, r_y))
    enter = 0
    not_enter = 0
    for key in result:
        if key <= radius**2:
            enter += 1
        else:
            not_enter += 1
    print('Точек внутри окружности:', enter, '\nВне окружности:', not_enter)
# Генератор случайных точек
x = np.random.random_integers(-99, 99, point)
y = np.random.random_integers(-99, 99, point)
r_x = []
r_y = []
calc()
os_x = []
os_y = []

# Поиск точек одного размера
def search():

    global os_x
    point = float(input('Введите координату для поиска точек на оси X: '))
    start = time.time()
    for key in x:
        if key == point:
            os_x.append(key)
    print('Найдено точек:', len(os_x))
    global os_y
    point = float(input('Введите координату для поиска точек на оси Y: '))
    for key in y:
        if key == point:
            os_y.append(key)
    print('Найдено точек:', len(os_y))
    len_x = len(os_x)
    if len(os_x) != len(y):
        os_y = os_y[:len_x]
    end = time.time()
    times.append(end - start)
    print('Время выполнения поиска точек:', *times)

# Цикл поиска точек
while radius > 0:
    search()
    break

# Лог времени
times = str(times)
file = open('timeLog.txt', 'w')
file.write(times)
file.close()

