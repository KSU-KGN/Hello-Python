"""
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""
def input_num(text):
    """
    Функция проверки правильности ввода
    @param text: текст приглашения к вводу
    @return: число
    """
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print('Требуется ввести число!')
            continue
        return number

def dividing(dividend, divider):
    """
    Функция выполняющая деление чисел,
    предусмотрена обработка ситуации деления на ноль
    @param dividend: делимое
    @param divider: делитель
    @return: результат деления или False при делении на 0
    """
    try:
        return dividend / divider
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        return False

number_1 = input_num('Введите делимое: ')
number_2 = input_num('Введите делитель: ')
result = dividing(number_1, number_2)
if result:
    print(f'{number_1} / {number_2} = {result:.2f}')
