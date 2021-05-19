# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """функция для вычисления суммы наибольших двух значений из трёх звдвнных"""
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + c
    elif c <= a and c <= b:
        return a + b

try:
    a_in = int(input("Введите первое число >>> "))
    b_in = int(input("Введите второе число >>> "))
    c_in = int(input("Введите третье число >>> "))
    print(f"сумма наибольших двух аргументов = {my_func(a_in, b_in, c_in)}")
except ValueError:
    print("Неверный ввод!")