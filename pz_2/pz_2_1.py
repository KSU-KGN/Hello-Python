"""
1) Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
my_list = ['список', 123, 1.23, True]
for i in my_list:
    print(f'Элемент "{i}" списка имеет тип {type(i)}')