# Задание 2

import sys

def ellipse_position(centre, radius, x, y):
    centre_x = centre[0]
    centre_y = centre[1]
    a = radius[0]   # Из условия задачи не совсем понятно, что именно из себя представляют «координаты радиуса».
    b = radius[1]   # По этой причине данные значения были использованы как длины полуосей.
    x = abs(x - centre_x)
    y = abs(y - centre_y)
    value = (x ** 2 / a ** 2) + (y ** 2 / b ** 2)
    if value == 1:
        return 0
    elif value < 1:
        return 1
    else:
        return 2

file1_path = input('Введите путь к 1-му файлу: ')
file2_path = input('Введите путь ко 2-му файлу: ')

ellipse_par = []
with open(file1_path, 'r') as file:
    for line in file:
        data = [int(x) for x in line.split()]
        ellipse_par.append(data)

points = []
counter = 0
with open(file2_path, 'r') as file:
    for line in file:
        data = [int(x) for x in line.split()]
        points.append(data)
        counter += 1
        if counter > 100:
            sys.exit('Во 2-ом файле количество пар координат превышает 100')

for point in points:
    print(ellipse_position(ellipse_par[0], ellipse_par[1], point[0], point[1]), end='\n')
