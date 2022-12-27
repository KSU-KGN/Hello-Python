"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы
получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    """
    Базовый класс Worker (работник) имеет атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут защищенный и ссылается на словарь,
    содержащий элементы: оклад и премия, например,
    {"wage": wage, "bonus": bonus}.
    """
    def __init__(self, user_name, user_surname, user_position,
                 user_wage, user_bonus):
        self.name = user_name
        self.surname = user_surname
        self.position = user_position
        self._income = {"wage": user_wage, "bonus": user_bonus}

class Position(Worker):
    """
    Дочерний класс базового класса Worker
    В классе Position реализованы методы:
    get_full_name
    get_total_income
    """
    def __init__(self, user_name, user_surname, user_position,
                 user_wage, user_bonus):
        super().__init__(user_name, user_surname, user_position,
                 user_wage, user_bonus)

    def get_full_name(self):
        """
        Получение полного имени сотрудника
        """
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        """
        Получение дохода с учетом премии
        """
        print(f'Доход с учетом премии: '
              f'{self._income["wage"] + self._income["bonus"]}')

user_class_1 = Position('Сергей', 'Иванов', 'директор', 500000, 50000)
user_class_1.get_full_name()
print(f'Должность: {user_class_1.position}')
user_class_1.get_total_income()
print('')
user_class_2 = Position('Пётр', 'Капица', 'научный сотрудник', 100000, 20000)
user_class_2.get_full_name()
print(f'Должность: {user_class_2.position}')
user_class_2.get_total_income()
