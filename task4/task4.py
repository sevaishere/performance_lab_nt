# Задание 4

import sys, statistics

def args_check(numb_of_args: int, args_rules: str):
    args_len = len(sys.argv[1:])
    if args_len < 1:
        sys.exit('Не введено ни одного аргумента.\n' + args_rules)
    elif args_len < numb_of_args:
        sys.exit('Введено слишком мало аргументов.\n' + args_rules)
    elif args_len > numb_of_args:
        sys.exit('Введено слишком много аргументов.\n' + args_rules)

def moves_to_equal(nums):
    median = int(statistics.median(nums))
    moves = 0
    for num in nums:
        moves += abs(num - median)
    if moves <= 20:
        return moves
    else:
        return '20-ти ходов недостаточно для приведения всех элементов массива к одному числу.'

args_check(1, 'В качестве аргумента необходимо ввести путь к файлу с массивом.')

file_path = sys.argv[1]

nums = []
with open(file_path, 'r') as file:
    for line in file:
        data = int(line.strip())
        nums.append(data)

print(moves_to_equal(nums))



