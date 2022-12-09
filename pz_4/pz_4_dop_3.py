"""
Дополнительные задания:
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randrange

def input_num_int(text):
    """
    Функция проверки правильности ввода
    @param text: текст приглашения к вводу
    @return: целое число
    """
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('Требуется ввести число!')
            continue
        return num

while True:
    user_number = input_num_int('Введите натуральное число: ')
    if user_number > 0:
        break
koef_list = [randrange(100) for index in range(user_number + 1)]
print(koef_list)
polynom = ''
sgn = False
for index, koef in enumerate(koef_list):
    if koef > 0:
        if sgn:
            polynom += " + "
        if index < user_number:
            if koef == 1:
                polynom += 'x'
            else:
                polynom += str(koef) + '*x'
            if index < user_number - 1:
                polynom += '^' + str(user_number - index)
        else:
            polynom += str(koef)
        if not sgn:
            sgn = True
polynom += ' = 0'
print(polynom)
