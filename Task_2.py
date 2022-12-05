# Задача № 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]
import Funk_for_2_3_task

num = int(input('Задайте натуральное число: '))


def finding_factors(n):
    """Cоставляет список простых множителей"""
    l = []
    div = 2
    while n > 1:
        if n % div == 0:
            l.append(div)
            n /= div
        else:
            div += 1
    return l


print('Cписок простых множителей:')
print(Funk_for_2_3_task.elem(finding_factors(num)))
