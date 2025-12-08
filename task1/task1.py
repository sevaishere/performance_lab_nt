# Задание 1

import sys

def args_check(numb_of_args: int, args_rules: str):
    args_len = len(sys.argv[1:])
    if args_len < 1:
        sys.exit('Не введено ни одного аргумента.\n' + args_rules)
    elif args_len < numb_of_args:
        sys.exit('Введено слишком мало аргументов.\n' + args_rules)
    elif args_len > numb_of_args:
        sys.exit('Введено слишком много аргументов.\n' + args_rules)

def circular_array(n, m):
    num = 1
    arr = []
    while True:
        arr.append(num)
        num = ((num + m - 2) % n) + 1
        if num == 1:
            break
    path = ''
    for i in arr:
        path = path + str(i)
    return path

args_check(4, 'Необходимо ввести 4 аргумента: '
              'параметры n и m сначала для первого массива, '
              'а затем для второго.')

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

output = circular_array(n1, m1) + circular_array(n2, m2)

print(output)
