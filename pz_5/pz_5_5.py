"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
from random import random
from functools import reduce

def my_summ(prev_el, el):
    """
    Функция суммы вещественных чисел
    @param prev_el: предшествующий элемент
    @param el: текущий элемент
    @return: результат суммы
    """
    return float(prev_el) + float(el)

with open('pz_5_5.txt', 'w', encoding='utf-8') as data_file:
    number = " ".join([str(round(random() * (10 - 1) + 1, 2)) for i in range(17)])
    print(f'Записываем в файл {data_file.name} набор чисел:\n{number}')
    data_file.writelines(number)
with open('pz_5_5.txt', 'r', encoding='utf-8') as data_file:
    number_list = data_file.read().split(" ")
print(f'Сумма чисел в файле равна {reduce(my_summ, number_list):.2f}')
