"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
что вы сделали и чего удалось добиться
Описания нужно делать в виде docstrings
"""
import sys
from memory_profiler import profile
import numpy as np
"""
Проверка скриптов
5) Реализовать формирование списка, кортежа и массива, используя
функцию range() и возможности генератора.
my_func_1_1(user_l, user_r) - формирование списка 1 (lc - List comprehensions).
my_func_1_2(user_l, user_r) - формирование списка 2 (list).
my_func_2(user_l, user_r) - формирование кортежа
my_func_3(user_l, user_r) - формирование массива
"""
@profile
def my_func_1_1(left, right):
    """
    Функция формирование списка четных чисел
    от left до right (включая границы)
    используя функцию range() и с помощью lc (List comprehensions)
    @param left: левая граница
    @param right: правая граница
    @return: сформированный список
    """
    arr = [item for item in range(left, right) if item % 2 == 0]
    return arr

@profile
def my_func_1_2(left, right):
    """
    Функция формирование списка четных чисел
    от left до right (включая границы)
    используя функцию range() и встроенную функцию list
    @param left: левая граница
    @param right: правая граница
    @return: сформированный список
    """
    arr = list(range(left, right, 2))
    return arr

@profile
def my_func_2(left, right):
    """
    Функция формирование кортежа четных чисел
    от left до right (включая границы)
    используя функцию range() и встроенную функцию tuple
    @param left: левая граница
    @param right: правая граница
    @return: сформированный кортеж
    """
    arr = tuple(range(left, right, 2))
    return arr

@profile
def my_func_3(left, right):
    """
    Функция формирование массива четных чисел
    от left до right (включая границы), использую возможности NumPy
    (numpy.ndarray)
    @param left: левая граница
    @param right: правая граница
    @return: сформированный массив
    """
    arr = np.arange(left, right, 2)
    return arr

user_left = 100
user_right = 100001
arr_list_1 = my_func_1_1(user_left, user_right)
arr_list_2 = my_func_1_2(user_left, user_right)
arr_tuple = my_func_2(user_left, user_right)
arr_nparray = my_func_3(user_left, user_right)
print(f"Размер списка arr_list_1:\n{sys.getsizeof(arr_list_1)} bytes")
print(f"Размер списка arr_list_2:\n{sys.getsizeof(arr_list_2)} bytes")
print(f"Размер списка arr_tuple:\n{sys.getsizeof(arr_tuple)} bytes")
print(f"Размер списка arr_nparray:\n{sys.getsizeof(arr_nparray)} bytes")
"""
Получили результат:
2.4 MiB или 444376 bytes
1.9 MiB или 399672 bytes
1.6 MiB или 399648 bytes
0.2 MiB или 199916 bytes
my_func_1_1(user_l, user_r) - список занимает больше всего места (lc)
my_func_1_2(user_l, user_r) - список занимает меньше места, если можно
использовать встроенную функцию list и возможность range с шагом 2
my_func_2(user_l, user_r) - кортеж занимает меньше места, чем список
my_func_3(user_l, user_r) - массив NumPy занимает меньше всего места
Вывод: меньше всего места в оперативной памяти занимает numpy.ndarray
"""
