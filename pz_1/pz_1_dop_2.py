"""
Дополнительные задания:
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
"""
def func_test(num_x, num_y, num_z):
    """Функция проверки истинности утверждения
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z"""
    left = not(num_x or num_y or num_z)
    right = not num_x and not num_y and not num_z
    return left == right

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if func_test(x, y, x):
                print(f'Для предикатов {x}, {y}, {z} выражение '
                      f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ИСТИНА')
            else:
                print(f'Для предикатов {x}, {y}, {z} выражение '
                      f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ЛОЖЬ')
