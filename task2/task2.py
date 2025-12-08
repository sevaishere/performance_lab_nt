# Задание 2

import sys

def args_check(numb_of_args: int, args_rules: str):
    args_len = len(sys.argv[1:])
    if args_len < 1:
        sys.exit('Не введено ни одного аргумента.\n' + args_rules)
    elif args_len < numb_of_args:
        sys.exit('Введено слишком мало аргументов.\n' + args_rules)
    elif args_len > numb_of_args:
        sys.exit('Введено слишком много аргументов.\n' + args_rules)

def ellipse_position(centre, radius, x, y):
    centre_x = centre[0]
    centre_y = centre[1]
    a = radius[0]   # Из условия задачи не совсем ясно, что именно из себя представляют «координаты радиуса».
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

args_check(2, 'Необходимо ввести 2 аргумента: '
              'сначала путь к файлу с параметрами эллипса, '
              'а затем путь к файлу с координатами точек.')

file1_path = sys.argv[1]
file2_path = sys.argv[2]

ellipse_par = []
with open(file1_path, 'r') as file:
    for line in file:
        data = [int(x) for x in line.split()]
        ellipse_par.append(data)

points = []
counter = 0
with open(file2_path, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            data = [int(x) for x in line.split()]
            points.append(data)
            counter += 1
            if counter > 100:
                sys.exit('В файле с координатами точек количество пар координат превышает 100')
        else:
            pass

for point in points:
    print(ellipse_position(ellipse_par[0], ellipse_par[1], point[0], point[1]), end='\n')
