"""
Тестирование модуля modul_9_4.py
"""
import unittest
from modul_9_4 import Cell

class TestPz92(unittest.TestCase):
    """
    TestCase для задания № 9_2
    """
    def setUp(self):
        """
        создаём объекты классов для тестирования
        """
        self.cell0 = Cell(0)
        self.cell1 = Cell(30)
        self.cell2 = Cell(25)

    def testexcept(self):
        """
        проверяем возможность появления исключения при заданных значений
        количества ячеек клетки
        """
        with self.assertRaises(Exception):
            self.cell1 / self.cell0

    def testmessage(self):
        """
        проверяем правильность вывода сообщения при выполнении вычитания.
        Потому что перацию необходимо выполнять только если разность количества
        ячеек двух клеток больше нуля,иначе выводить соответствующее сообщение.
        """
        self.assertEqual(self.cell2 - self.cell1,
                         "Разность отрицательная, "
                         "поэтому операция не выполняется")

if __name__ == '__main__':
    unittest.main()
