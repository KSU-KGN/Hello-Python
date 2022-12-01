"""
Дополнительные задания:
    Напишите программу, которая принимает на вход число N и
    выдает набор произведений чисел от 1 до N.
    Пример:
    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
def input_num(text):
    """
    Функция проверки правильности ввода
    @param text: текст приглашения к вводу
    @return: число
    """
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('Требуется ввести число!')
            continue
        return num

while True:
    number = input_num('Введите целое число большее 0: ')
    if number > 0:
        break
my_list =[]
for index in range(number):
    result = 1
    for i in range(2, index+2):
        result *= i
    my_list.append(result)
print(f'Набор произведений чисел от 1 до {number}: {my_list}')
