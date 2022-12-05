"""
2) Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def print_user_date(name, surname, birthday, city, email, phone):
    """
    Функция реализует вывод данных о пользователе одной строкой
    @param name: имя
    @param surname: фамилия
    @param birthday: год рождения
    @param city: город проживани
    @param email: email
    @param phone: телефон
    """
    print(f'{name}, {surname}, {birthday}, {city}, {email}, {phone}')

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birthday = input('Введите год рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phone = input('Введите телефон: ')
print_user_date(surname=user_surname, name=user_name, phone=user_phone,
                birthday=user_birthday, city=user_city, email=user_email)
