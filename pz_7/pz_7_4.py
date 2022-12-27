"""
4) Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    """
    Базовый класс имеет атрибуты:
    speed, color, name, is_police (булево).
    Методы: go, stop, turn(direction), которые сообщают,
    что машина поехала, остановилась, повернула (куда).
    """
    def __init__(self, speed, color, name, is_police = None):
        """
        Метод __init__ атрибуты класса передаются при создании экземпляра класса
        @param speed: скорость
        @param color: цвет
        @param name: марка
        @param is_police: является ли полицейской машиной
        """
        self.speed = speed
        self.color = color
        self.name = name
        if is_police is None:
            self.is_polise = False
        else:
            self.is_polise = True

    @staticmethod
    def go():
        """
        Метод сообщает, что машина поехала
        """
        print("Машина поехала.")

    @staticmethod
    def stop():
        """
        Метод сообщает, что машина остановилась
        """
        print("Машина остановилась.")

    @staticmethod
    def turn(direction):
        """
        Метод сообщает, что машина повернула (куда)
        @param direction: куда повернула машина
        """
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        """
        Метод показывает текущую скорость автомобиля
        """
        print(f'Текущая скорость {self.name} автомобиля {self.speed}')

    def __str__(self):
        print(f'Машина {self.name} цвет {self.color}')
        self.go()
        self.turn('налево')
        self.show_speed()
        self.stop()
        if self.is_polise:
            return 'Это полицейская машина!'
        else:
            return 'Это НЕ полицейская машина.'


class TownCar(Car):
    """
    Дочерний класс базового класса Car
    """
    def __init__(self, speed, color, name, is_police = None):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """
        Переопределяет метод show_speed базового класса Car
        Метод показывает текущую скорость автомобиля
        При значении скорости свыше 60 (TownCar) выводится сообщение
        о превышении скорости.
        """
        print(f'Текущая скорость городского автомобиля {self.speed}')
        if self.speed > 60:
            print("Превышение скорости!")

class SportCar(Car):
    """
    Дочерний класс базового класса Car
    """
    def __init__(self, speed, color, name, is_police = None):
        super().__init__(speed, color, name, is_police)

    def __str__(self):
        print(f'Машина {self.name} цвет {self.color}')
        self.go()
        self.turn('направо')
        self.show_speed()
        self.stop()
        if self.is_polise:
            return 'Это полицейская машина!'
        else:
            return 'Это спортивная машина.'

class WorkCar(Car):
    """
    Дочерний класс базового класса Car
    """
    def __init__(self, speed, color, name, is_police = None):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """
        Переопределяет метод show_speed базового класса Car
        Метод показывает текущую скорость автомобиля
        При значении скорости свыше 40 (WorkCar) выводится сообщение
        о превышении скорости.
        """
        print(f'Текущая скорость рабочего автомобиля {self.speed}')
        if self.speed > 40:
            print("Превышение скорости!")

class PoliceCar(Car):
    """
    Дочерний класс базового класса Car
    """
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name, is_police)

    def __str__(self):
        print(f'Машина {self.name} цвет {self.color}')
        self.go()
        self.turn('по кольцу')
        self.show_speed()
        self.stop()
        if self.is_polise:
            return 'Это полицейская машина!'
        else:
            return 'Это спортивная машина.'

user_class_1 = TownCar(70, 'yellow', 'Audi')
print(user_class_1, '\n')
user_class_2 = WorkCar(50, 'white', 'BMW')
print(user_class_2, '\n')
user_class_3 = PoliceCar(100, 'black', 'Ford', True)
print(user_class_3, '\n')
user_class_4 = SportCar(120, 'red', 'Ferrari')
print(user_class_4, '\n')
