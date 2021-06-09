# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    complex_num: tuple

    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        return ((self.complex_num[0] + other.complex_num[0]), (self.complex_num[1] + other.complex_num[1]))

    def __mul__(self, other):
            return (
                    self.complex_num[0] * other.complex_num[0] - self.complex_num[1] * other.complex_num[1],
                    self.complex_num[1] * other.complex_num[0] + self.complex_num[0] * other.complex_num[1]
                    )

    @classmethod
    def input_nums(cls):
        real_num: int
        imaginary_num: int
        try:
            real_num = int(input("Введите действительную часть >>>"))
            imaginary_num = int(input("Введите мнимую часть >>>"))
        except ValueError:
            print("Ошибка ввода")
            exit()
        complex_num = (real_num, imaginary_num)
        return complex_num


first_complex_number = ComplexNumber(ComplexNumber.input_nums())
second_complex_number = ComplexNumber(ComplexNumber.input_nums())

print(f"Введены комплексные числа: {first_complex_number.complex_num} и {second_complex_number.complex_num}")
print(f"Сумма комплексных чисел: {first_complex_number.__add__(second_complex_number)}")
print(f"Произведение комплексных чисел: {first_complex_number.__mul__(second_complex_number)}")





