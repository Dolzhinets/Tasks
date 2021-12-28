# 2. Написать функцию для вычисления суммы всех 
# элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): 
# [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

my_list = [[1, 9, 8, 7, 4], [7, [3, 12, [2, 7]]], [2, 1]]

def sum_el_list(my_list):
    total = 0
    for el in my_list:
        if isinstance(el, list):
            total += sum_el_list(el)
        else:
            total += el
    return total

print("Сумма элементов списка =", sum_el_list(my_list)) 