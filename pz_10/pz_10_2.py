"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""
class MySingleton(type):
    """
    Метакласс MySingleto: для класса может быть добавлен только один экземпляр,
    все новые вызовы конструктора объекта будут возвращать созданный ранее
    (первый) экземпляр
    """
    def __init__(cls, *args, **kwargs):
        """
        При инициализации у каждого подконтрольного класса
        в приватном атрибуте __first хранится ссылка на первый созданный
        экземпляр класса (первоначально - None)
        """
        cls.__first = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        При создании объекта класса, если ещё не создан первый экземлар класса,
        то создаём его. В противном случае не создаём экземпляр класса.
        @return: возвращаем ссылку на первый созданный экземпляр класса
        """
        if cls.__first is None:
            cls.__first = super().__call__(*args, **kwargs)
        return cls.__first

class MyClassProba():
    """
    MyClassProba - обычный класс
    """
    def __init__(self):
        print('Класс MyClassProba')


class MyClass_1(metaclass=MySingleton):
    """
    Класс MyClass1 использует возможности метакласса  MySingleton
    """
    def __init__(self):
        print('Класс MyClass_1')

class MyClass_2(metaclass=MySingleton):
    """
    Класс MyClass2 использует возможности метакласса  MySingleton
    """
    def __init__(self):
        print('Класс MyClass_2')

my_proba_1 = MyClassProba()
my_proba_2 = MyClassProba()
print('my_proba_1 и my_proba_2 являются ДВУМЯ различными объектами '
      'обычного класса MyClassProba()')
print(f'my_proba_1 is my_proba_2 = {my_proba_1 is my_proba_2}\n')
my_obj_1_1 = MyClass_1()
my_obj_1_2 = MyClass_1()
print('my_obj_1_1 и my_obj_1_2 являются одним и тем же объектом '
      'изменённого класса MyClass_1(metaclass=MySingleton)')
print(f'my_obj_1_1 is my_obj_1_2 = {my_obj_1_1 is my_obj_1_2}\n')
my_obj_2_1 = MyClass_2()
my_obj_2_2 = MyClass_2()
print('my_obj_2_1 и my_obj_2_2 являются одним и тем же объектом '
      'изменённого класса MyClass_2(metaclass=MySingleton)')
print(f'my_obj_2_1 is my_obj_2_2 = {my_obj_2_1 is my_obj_2_2}\n')
print('Объекты разных классов MyClass_1 и MyClass_2 различны!')
print(f'my_obj_1_1 is my_obj_2_1 = {my_obj_1_1 is my_obj_2_1}')
print(f'my_obj_1_2 is my_obj_2_2 = {my_obj_1_2 is my_obj_2_2}')
