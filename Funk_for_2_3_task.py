def elem(n):
    """Собираем список не повторяющихся элементов"""
    l = []
    [l.append(i) for i in n if i not in l]
    return l
