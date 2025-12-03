# Задание 4

import statistics

def moves_to_equal(nums):
    median = int(statistics.median(nums))
    moves = 0
    for num in nums:
        moves += abs(num - median)
    if moves <= 20:
        return moves
    else:
        return '20-ти ходов недостаточно для приведения всех элементов массива к одному числу'

file_path = input('Введите путь к файлу: ')

nums = []
with open(file_path, 'r') as file:
    for line in file:
        data = int(line.strip())
        nums.append(data)

print(moves_to_equal(nums))



