"""
5) Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""
debit = float(input('Введите выручку фирмы: '))
credit = float(input('Введите издержки фирмы: '))
if debit > credit:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки равна {debit / credit}')
    number = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна '
          f'{(debit - credit) / number}')
else:
    print('Фирма работает в убыток')