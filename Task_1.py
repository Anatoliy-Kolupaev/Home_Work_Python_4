# Задача № 1
# Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
from math import pi

# Если передается целое число

n = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {n} равно {round(pi, n)}')


# Если передается как в примере

n = input("Введите число для заданной точности числа Пи:\n")
print(f'число Пи с заданной точностью {n} равно {round(pi, len(n) - 2)}')