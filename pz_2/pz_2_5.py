"""
5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
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

my_list = [7, 5, 3, 3, 2]
print(f'Существующий рейтинг: {my_list}')
new_rating = input_num('Введите новый элемент рейтинга: ')
for i, item in enumerate(my_list):
    if new_rating > item:
        my_list.insert(i, new_rating)
        break
    if i == len(my_list) - 1:
        my_list.insert(i + 1, new_rating)
        break
print(f'Новый рейтинг: {my_list}')
