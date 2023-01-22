"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
class FoundCyrillics(Exception):
    """
    Собственный класс-исключение, обрабатывающий ситуацию преобразования
    не ascii-символов
    """
    def __init__(self, txt):
        """
        Конструктор инициализирует параметр (txt)
        @param txt: текст ошибки
        """
        self.txt = txt

try:
    worlds = ['attribute', 'класс', 'функция', 'type']
    result = []
    for world in worlds:
        if world.isascii():
            print(f"{world} - возможно записать в байтовом типе с помощью "
                  f"маркировки b'' (без encode decode)")
        else:
            result.append(world)
    if len(result) > 0:
        raise FoundCyrillics(f"{result} невозможно записать в байтовом типе с "
                             f"помощью маркировки b'' (без encode decode)")
except FoundCyrillics as error:
    print(error)
