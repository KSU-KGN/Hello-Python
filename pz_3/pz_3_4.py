"""
4) Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *,
предусматривающая использование цикла.
"""
def my_func_1(x, y):
    """
    Функция возведения числа x в степень y
    Первый способ — возведение в степень с помощью оператора *
    @param x: действительное положительное число  x
    @param y: целое отрицательное число
    @return: результат возведения числа в степень
    """
    return x**y

def my_func_2(x, y):
    """
    Функция возведения числа x в степень y
    Второй способ — более сложная реализация без оператора *,
    @param x: действительное положительное число  x
    @param y: целое отрицательное число
    @return: результат возведения числа в степень
    """
    result = 1
    for repetition in range(-y):
        result /= x
    return result

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

def input_num_float(text):
    """
    Функция проверки правильности ввода
    @param text: текст приглашения к вводу
    @return: действительное число
    """
    while True:
        try:
            num = float(input(text))
        except ValueError:
            print('Требуется ввести число!')
            continue
        return num

while True:
    number_x = input_num_float('Введите действительное положительное число: ')
    if number_x > 0.0:
        break
while True:
    number_y = input_num_int('Введите целое отрицательное число: ')
    if number_y < 0:
        break
print(f'{number_x} в степени {number_y} равно '
      f'{my_func_1(number_x, number_y):.5f}')
print(f'{number_x} в степени {number_y} равно '
      f'{my_func_2(number_x, number_y):.5f}')
