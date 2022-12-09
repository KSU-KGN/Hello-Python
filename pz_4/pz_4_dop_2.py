"""
Дополнительные задания:
Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N.
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

def simple(number):
    """
    Функция нахождения простых множителей числа
    @param number: число
    @return: список простых множителей числа
    """
    result = []
    my_end = int(number**0.5)
    for item in range(2, my_end):
        if number % item == 0:
            result.append(item)
            while number % item == 0:
                number //= item
    if number > 1:
        result.append(number)
    return result

while True:
    user_number = input_num_int('Введите натуральное число: ')
    if user_number > 0:
        break
print(simple(user_number))
