"""
Дополнительные задания:
    Задайте число. Составьте список чисел Фибоначчи,
    в том числе для отрицательных индексов.
    Пример:
    для k = 8 список будет выглядеть так:
    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
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

def fibonacci(number):
    """
    Функция нахождения чисел Фибоначчи,
    в том числе для отрицательных индексов
    @param number: индекс числа
    @return: число Фибоначчи
    """
    if number in range(2):
        return number
    if user_number + number < len(result):
        return result[user_number + number]
    if number > 0:
        return fibonacci(number - 1) + fibonacci(number - 2)
    return fibonacci(number + 2) - fibonacci(number + 1)

while True:
    user_number = input_num_int('Введите целое положительное число: ')
    if user_number > 0:
        break
result = []
for item in range(-user_number, user_number + 1):
    result.append(fibonacci(item))
print(result)
