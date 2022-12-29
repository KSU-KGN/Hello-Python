"""
Тестирование модуля modul_9_2.py
"""
import unittest
from modul_9_2 import Car, TownCar, SportCar, PoliceCar

class TestPz74(unittest.TestCase):
    """
    TestCase для задания № 7_4
    """
    def setUp(self):
        """
        создаём объекты классов для тестирования
        """
        self.item_1 = TownCar(70, 'yellow', 'Audi')
        self.item_2 = PoliceCar(100, 'black', 'Ford', True)

    def testparent(self):
        """
        проверяем является ли объект класса экземпляром (потомком) класса Car
        """
        self.assertIsInstance(self.item_1, Car)

    def testnotparent(self):
        """
        проверяем, чтобы объект класса не являлся экземпляром класса SportCar
        """
        self.assertNotIsInstance(self.item_1, SportCar)

    def testispolice(self):
        """
        проверяем является ли машина полицейской
        """
        self.assertTrue(self.item_2.is_polise)

    def testisnotpolice(self):
        """
        проверяем, чтобы машина не являлась полицейской
        """
        self.assertFalse(self.item_1.is_polise)

if __name__ == '__main__':
    unittest.main()
