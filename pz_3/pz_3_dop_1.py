"""
Дополнительные задания:
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
user_list = [2, 3, 5, 9, 3, 7]
result = 0
user_number = ''
for item, number in enumerate(user_list):
    if item % 2 != 0:
        result += number
        if item < len(user_list) - 2:
            user_number += str(number) + ', '
        else:
            user_number += str(number)
print(f'Сумма элементов списка ({user_number}), стоящих на нечётной позиции '
      f'равна {result}')
