"""
Задание 3.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivZero(Exception):
    """
    Собственный класс-исключение, обрабатывающий ситуацию деления на ноль
    """
    def __init__(self, txt):
        """
        Конструктор инициализирует параметр (txt)
        @param txt: текст ошибки
        """
        self.txt = txt

try:
    number_1 = int(input('Введите делимое: '))
    number_2 = int(input('Введите делитель: '))
    if number_2 == 0:
        raise DivZero('На ноль делить нельзя!')
except DivZero as error:
    print(error)
except ValueError:
    print('Требуется ввести число!')
else:
    print(f'{number_1} / {number_2} = {number_1 / number_2}')
