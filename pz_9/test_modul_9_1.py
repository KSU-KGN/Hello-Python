"""
Тестирование модуля modul_9_1.py
"""
import unittest
from modul_9_1 import Road

class TestPz72(unittest.TestCase):
    """
    TestCase для задания № 7_2
    """
    def setUp(self):
        """
        создаём объект класса для тестирования
        """
        self.calc = Road(5000, 20)

    def testcalcmass(self):
        """
        проверяем правильность расчёта массы асфальта, необходимого для
        покрытия всего дорожного полотна
        """
        self.assertEqual(self.calc.calc_mass(), 125000)

    def testthickness(self):
        """
        проверяем правильно толщины полотна:
        должна быть не 5 см, а 0.05 м
        """
        self.assertNotEqual(self.calc.thickness, 5)

if __name__ == '__main__':
    unittest.main()
