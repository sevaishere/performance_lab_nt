# Задание 1

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

n1 = int(input('Введите параметр «n» для 1-го массива: '))
m1 = int(input('Введите параметр «m» для 1-го массива: '))
n2 = int(input('Введите параметр «n» для 2-го массива: '))
m2 = int(input('Введите параметр «m» для 2-го массива: '))

output = circular_array(n1, m1) + circular_array(n2, m2)

print(output)
