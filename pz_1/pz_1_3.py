"""
3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
#Вариант 2: для любых положительных чисел
num_str = input('Введите число: ')
number_1 = int(num_str)
number_2 = int(num_str + num_str)
number_3 = int(num_str + num_str + num_str)
summer = number_1 + number_2 + number_3
print(f'{number_1} + {number_2} + {number_3} = {summer}')

"""
#Вариант 1: для чисел от 1 по 9 
number_1 = int(input('Введите число: '))
number_2 = number_1 * 10 + number_1
number_3 = number_2 * 10 + number_1
summer = number_1 + number_2 + number_3
print(f'{number_1} + {number_2} + {number_3} = {summer}')
"""
