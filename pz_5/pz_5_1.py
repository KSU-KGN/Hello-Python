"""
1) Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print('Вводите данные построчно. Окончание ввода - пустая строка')
with open('pz_5_1.txt', 'w', encoding='utf-8') as data_file:
    while True:
        user_str = input()
        if user_str != '':
            data_file.write(user_str + '\n')
        else:
            break
