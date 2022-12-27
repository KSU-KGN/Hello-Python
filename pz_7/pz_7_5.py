"""
5) Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    """
    Класс Stationery (канцелярская принадлежность)
    """
    def __init__(self, user_title):
        self.title = user_title

    def draw(self):
        """
        Метод draw (отрисовка) выводит сообщение “Запуск отрисовки.”
        """
        print("Запуск отрисовки.")

class Pen(Stationery):
    """
    Дочерний класс Pen (ручка) базавого класса Stationery
    """
    def __init__(self, user_title):
        super().__init__(user_title)

    def draw(self):
        """
        Переопределяет метод draw базового класса
        Метод draw (отрисовка) выводит сообщение “Запуск отрисовки ручкой.”
        """
        print(f'Это {self.title}.\nЗапуск отрисовки ручкой.')


class Pencil(Stationery):
    """
    Дочерний класс Pencil (карандаш) базавого класса Stationery
    """
    def __init__(self, user_title):
        super().__init__(user_title)

    def draw(self):
        """
        Переопределяет метод draw базового класса
        Метод draw (отрисовка) выводит сообщение “Запуск отрисовки карандашом.”
        """
        print(f'Это {self.title}.\nЗапуск отрисовки карандашом.')

class Handle(Stationery):
    """
    Дочерний класс Handle (маркер) базавого класса Stationery
    """
    def __init__(self, user_title):
        super().__init__(user_title)

    def draw(self):
        """
        Переопределяет метод draw базового класса
        Метод draw (отрисовка) выводит сообщение “Запуск отрисовки маркером.”
        """
        print(f'Это {self.title}.\nЗапуск отрисовки маркером.')

user_pen = Pen('ручка')
user_pen.draw()
user_pencil = Pencil('карандаш')
user_pencil.draw()
user_handle = Handle('маркер')
user_handle.draw()
