# Задача № 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
#     k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
#     k=3 => 2*x^3 + 4*x^2 + 4*x + 5

import random

degree = int(input('Введите натуральную степень k: '))


def write_file(s):
    """Записывает результат в файл"""
    with open('Task_4_result.txt', 'w') as data:
        data.write(s)


def create_koeff(n):
    """Формирует случайным образом список коэффициентов"""
    lst = []
    for i in range(n + 1):
        lst.append(random.randint(0, 101))
    return lst


def create_result(s):
    """Создает многочлен в степени k"""
    list = s[::-1]
    str = ''
    if len(list) < 1:
        str = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                str += f'{list[i]}x**{len(list) - i - 1}'
                if list[i + 1] != 0:
                    str += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                str += f'{list[i]}x'
                if list[i + 1] != 0:
                    str += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                str += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                str += ' = 0'
    return str


koeff = create_koeff(degree)
print('Список коэффициентов', koeff)
print(create_result(koeff))
write_file(create_result(koeff))
