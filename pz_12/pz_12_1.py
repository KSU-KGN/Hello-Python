"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    main_data.append(["Изготовитель системы", "Название ОС", "Код продукта",
                 "Тип системы"])
    for i in range(1, 4):
        with open(f"info_{i}.txt") as f_name:
            data = f_name.read()
            # Получаем список изготовителей системы
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            prod_add = os_prod_reg.findall(data)[0].split()[2]
            os_prod_list.append(prod_add)
            # Получаем список названий ОС
            #os_name_reg = re.compile(r'Название ОС:\s*\S*\s\S*\s\S*')
            #os_name_list.append(os_name_reg.findall(date)[0].split()[2:7])
            os_name_reg = re.compile(r'Microsoft Windows\s\S*')
            name_add = os_name_reg.findall(data)[0]
            os_name_list.append(name_add)
            # Получаем список кодов продукта
            os_code_reg = re.compile(r'Код продукта:\s*\S*')
            code_add = os_code_reg.findall(data)[0].split()[2]
            os_code_list.append(code_add)
            # Получаем список типов системы
            os_type_reg = re.compile(r'Тип системы:\s*\S*')
            type_add = os_type_reg.findall(data)[0].split()[2]
            os_type_list.append(type_add)
            main_data.append([prod_add, name_add, code_add, type_add])
    return main_data

def write_to_csv():
    csv_date = get_data()
    with open("test_file.csv", 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in csv_date:
            csv_writer.writerow(row)
    with open("test_file.csv", 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

write_to_csv()
