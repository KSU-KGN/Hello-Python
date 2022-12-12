"""
3) Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
summa_salary = 0
count_emp = 0
with open('pz_5_3.txt', 'r', encoding='utf-8') as data_file:
    for line in data_file:
        fio, salary = line.split(' ')
        salary = float(salary[:-1])
        if salary < 20000.00:
            print(fio)
        summa_salary += salary
        count_emp += 1
print(f'Средняя величина дохода сотрудников равна {summa_salary / count_emp}')
