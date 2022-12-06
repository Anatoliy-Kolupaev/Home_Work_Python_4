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

# вариант 2

def dividers(a: int, uniq: bool = False) -> list[int]:
    """"Возвращает список простых делителей числа.
    uniq = True вернет список уникальных делителей"""
    i = 2
    dividers = []
    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers


a = 81
print(f'Список натуральных делителей числа {a}:{dividers(a)}')
print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')
