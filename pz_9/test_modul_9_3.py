"""
Тестирование модуля modul_9_3.py
"""
import unittest
from modul_9_3 import creat_list

class TestPz42(unittest.TestCase):
    """
    TestCase для задания № 4_2
    """
    def setUp(self):
        """
        заполняем данные для тестирования
        """
        self.user = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
        self.result = [12, 44, 4, 10, 78, 123]
        self.notresult = [300, 1, 1, 7, 55]

    def testresult(self):
        """
        проверяем результат, все полученные значения в списке должны входить
        в результирующий список с результатами
        """
        for item in creat_list(self.user):
            self.assertIn(item, self.result)

    def testnotresult(self):
        """
        проверяем результат, все полученные значения в списке НЕ должны входить
        в список невошедших значений
        """
        for item in creat_list(self.user):
            self.assertNotIn(item, self.notresult)

if __name__ == '__main__':
    unittest.main()
