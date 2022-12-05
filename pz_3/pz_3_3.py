"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def input_num(text):
    """
    Функция проверки правильности ввода
    @param text: текст приглашения к вводу
    @return: число
    """
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('Требуется ввести число!')
            continue
        return num

def my_func(arg_1, arg_2, arg_3):
    """
    Функция, которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов
    @param arg_1: аргумент 1
    @param arg_2: аргумент 2
    @param arg_3: аргумент 3
    @return: возвращает сумму наибольших двух аргументо
    """
    result = None
    if arg_1 < arg_2 and arg_1 < arg_3:
        result = arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        result = arg_1 + arg_3
    else:
        result = arg_1 + arg_2
    return result

number_1 = input_num('Введите 1 число: ')
number_2 = input_num('Введите 2 число: ')
number_3 = input_num('Введите 3 число: ')
print(f'Сумма наибольших двух чисел равна {my_func(number_1, number_2, number_3)}')
