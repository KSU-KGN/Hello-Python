"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""
from sys import argv

def salary(hours, rate, award):
    """
    Функция расчета заработной платы сотрудника
    @param hours: выработка в часах
    @param rate: ставка в час
    @param award: премия
    @return: заработной платы сотрудника по формуле:
             (выработка в часах*ставка в час) + премия
    """
    return hours * rate + award

script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)
print(f'Заработная плата сотрудника равна '
      f'{salary(int(first_param), int(second_param), int(third_param))}')
