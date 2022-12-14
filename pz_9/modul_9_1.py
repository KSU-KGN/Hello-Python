"""
2) Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
!!! Сантиметры переводим в метры и получаем 125 тонн !!!
"""
class Road:
    """
    Класс Road (дорога) имеет защищенные атрибуты:
    length (длина), width (ширина).
    Метод calc_mass: расчет массы асфальта, необходимого для покрытия всего
                     дорожного полотна.
    """
    weight = 25
    thickness = 0.05

    def __init__(self, user_length, user_width):
        """
        Метод __init__ атрибуты класса передаются при создании экземпляра класса
        @param user_length: length (длина)
        @param user_width: width (ширина)
        """
        self._length = user_length
        self._width = user_width

    def calc_mass(self):
        """
        Метод calc_mass - метод расчета массы асфальта, необходимого
        для покрытия всего дорожного полотна.
        @return: масса асфальта, необходимого для покрытия всего
        дорожного полотна в кг
        """
        return self._length * self._width * Road.weight * Road.thickness
"""
length = 5000
width = 20
user_class = Road(length, width)
print(f'Длина дороги {length} м, ширина дороги {width} м\nМасса асфальта для '
      f'покрытия одного кв метра дороги асфальтом {user_class.weight} кг\n'
      f'Число см толщины полотна {user_class.thickness} м')
result = user_class.calc_mass()
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна\n'
      f'{result} кг или {result / 1000} т\n')
"""