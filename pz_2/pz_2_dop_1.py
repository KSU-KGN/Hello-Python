"""
Дополнительные задания:
    Напишите программу, которая принимает на вход вещественное число
    и показывает сумму его цифр.
    Пример:
    6782 -> 23
    0,56 -> 11
"""
def test_num(num):
    """
    Функция проверки правильности ввода
    @param num: проверяемое число
    @return: результат проверки
    """
    while True:
        try:
            float(num)
            return True
        except ValueError:
            print('Требуется ввести вещественное число!')
            return False

while True:
    number = input('Введите вещественное число: ')
    if test_num(number):
        break
summa = 0
for item in number:
    if item.isdigit():
        summa += int(item)
print(f'Сумма цифр числа равна {summa}')
