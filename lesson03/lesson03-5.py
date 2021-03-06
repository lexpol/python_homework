# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def user_input():
    """Функция для ввода строки чисел разделенных пробелом и преобразования в кортеж"""
    string_in = str(input("введите строку чисел, разделенных пробелом, выход(Q) >>> "))
    return string_in.split()
try:
    total = 0
    while True:
        for i in user_input():
            if i.capitalize() == "Q":
                print(f"Сумма введенных элементов: {total}")
                exit()
            total += int(i)
        print(f"Сумма введенных элементов: {total}")
except ValueError:
    print("Ошибка ввода")