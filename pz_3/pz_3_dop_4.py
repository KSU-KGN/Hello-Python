"""
Дополнительные задания:
    Напишите программу, которая будет преобразовывать десятичное число
    в двоичное.
    Пример:
    45 -> 101101
    3 -> 11
    2 -> 10
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

user_number = input_num_int('Введите целое число: ')
if user_number < 0:
    sign = -1
else:
    sign = 1
number = sign * user_number
result = ''
while number // 2 > 0:
    result += str(number % 2)
    number //= 2
result += str(number % 2)
print(f'{user_number} -> {result[::-1]}')
