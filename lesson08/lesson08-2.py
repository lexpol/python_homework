# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivZeroException(Exception):
    def __str__(self):
        return "Деление на ноль!"

class Division:
    dividend: int
    divider: int

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def div(self):
        if self.divider == 0:
            raise DivZeroException
        else:
            return self.dividend / self.divider
try:
    a = int(input("Введите делимое >>>"))
    b = int(input("Введите делитель >>>"))
except ValueError:
    print("неверный формат!")

example = Division(a, b)


try:
    print(f"результат: {example.div()}")
except DivZeroException as exception:
    print("Деление на ноль!!")


