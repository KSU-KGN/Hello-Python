"""
3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print([item for item in range(20, 240) if item % 20 == 0 or item % 21 == 0])
