"""
Дополнительные задания:
Вычислить число пи c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164
"""
def calc_pi(eps):
    """
    Функция вычисления число пи c заданной точностью
    @param eps: точность
    @return: число пи
    """
    result = 0
    denom = 1
    sgn = 1
    while True:
        item = 4 / denom
        result += sgn * item
        if item <= eps:
            break
        sgn *= -1
        denom += 2
    return result

my_eps = 0.000001
number = my_eps
count = 0
while number < 1:
    number *= 10
    count += 1
print(f'Число пи c точностью {my_eps:.{count}f} '
      f'равно {calc_pi(my_eps):.{count}f}')
