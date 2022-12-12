"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('pz_5_2.txt', 'r', encoding='utf-8') as data_file:
    str_list = data_file.readlines()
str_count = 0
for item in str_list:
    str_count += 1
    str_len = len(item.split(' '))
    print(f'{str_count} строка "{item[:-1]}" содержит {str_len} слов')
print(f'Итого {str_count} строк')
