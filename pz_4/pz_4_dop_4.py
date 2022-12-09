"""
Дополнительные задания:
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
def creat_dict(line_list):
    """
    Функция создания словаря полинома из списка
    @param line_list: список
    @return: словарь полинома
    """
    result = {}
    for item in line_list:
        index = item.find('x')
        if index != -1:
            index_koef = item.find('*')
            if index_koef != -1:
                koef = int(item[:index_koef])
            else:
                koef = 1
            index_deg = item.find('^')
            if index_deg != -1:
                degree = int(item[index_deg + 1])
            else:
                degree = 1
        else:
            degree = 0
            koef = int(item)
        result[degree] = koef
    return result

def print_polynom(res):
    """
    Функция создания строки с полиномом
    @param res: словарь полинома
    @return: строка с полиномом
    """
    polynom = ''
    sgn = False
    for key_def, value_def in res.items():
        if sgn:
            polynom += " + "
        if key_def > 0:
            if value_def == 1:
                polynom += 'x'
            else:
                polynom += str(value_def) + '*x'
            if key_def > 1:
                polynom += '^' + str(key_def)
        else:
            polynom += str(value_def)
        if not sgn:
            sgn = True
    polynom += ' = 0'
    return polynom

with open('file1.txt', 'r', encoding="utf-8") as data_1:
    for line in data_1:
        print(f'Запись многочлена из 1-го файла\n{line}')
        line = line[:-4]
        line_1_list = line.split(' + ')
with open('file2.txt', 'r', encoding="utf-8") as data_2:
    for line in data_2:
        print(f'Запись многочлена из 2-го файла\n{line}')
        line = line[:-4]
        line_2_list = line.split(' + ')
res_1 = creat_dict(line_1_list)
res_2 = creat_dict(line_2_list)
res_itog = res_1.copy()
flag = False
for key, value in res_2.items():
    if key in res_itog:
        res_itog[key] += value
    else:
        res_itog[key] = value
        flag = True
if flag:
    res_itog = dict(sorted(res_itog.items(), key=lambda x: x[0], reverse=True))
res_str = print_polynom(res_itog)
print(f'Cумма многочленов:\n{res_str}')
with open('result.txt', 'w', encoding="utf-8") as data_res:
    data_res.write(res_str)
