"""
6) Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение
элементов списка будет прекращено.
"""
from itertools import count, cycle

def generate_int(start_number, end_number):
    """
    Функция-итератор, генерирующий целые числа
    @param start_number: начало списка
    @param end_number: конец списка (включительно)
    @return: список целых чисел
    """
    result = []
    for item in count(start_number):
        if item > end_number:
            break
        result.append(item)
    return result

def repeat_int(user_list, end_number):
    """
    Функция-итератор, повторяющий элементы списка
    @param user_list: список
    @param end_number: количество элементов списка для повтора
    @return: список с повторяющимися элементами
    """
    counter = 0
    result = []
    for item in cycle(user_list):
        if counter == end_number:
            break
        result.append(item)
        counter += 1
    return result

my_list = generate_int(3, 10)
my_repeat = len(my_list) * 3 - 3
print(f'Список целых чисел c 3 по 10 \n{my_list}')
print(f'Список повторяющий элементы вышеуказанного списка {my_repeat} раз\n'
      f'{repeat_int(my_list, my_repeat)}')
