# Задача № 5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy

with open('Task_5_1.txt', 'r') as data:
    str1 = sympy.sympify(data.read())
print(str1)

with open('Task_5_2.txt', 'r') as data:
    str2 = sympy.sympify(data.read())
print(str2)
print(sympy.simplify(str1 + str2))

with open('Task_5_result.txt', 'w') as data:
    data.write(str(sympy.simplify(str1 + str2)))
