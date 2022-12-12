"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
number_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []
with open('pz_5_4.txt', 'r', encoding='utf-8') as data_file:
    for line in data_file:
        line_list = line.split(' ')
        for index, item in enumerate(line_list):
            if item in number_dict:
                line_list[index] = number_dict[item]
        result.append(" ".join(line_list))
with open('pz_5_4_itog.txt', 'w', encoding='utf-8') as data_file:
    data_file.writelines(result)
