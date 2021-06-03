# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    matrix: list

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for row in self.matrix:
            for item in row:
                result += f"{item} "
            result += "\n"
        return result

    def __add__(self, other):
        result_matrix = []
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print("разный размер матриц, сложение невозможно")
            return None
        for line in range(len(self.matrix)):
            newline = []
            for item in range(len(self.matrix[line])):
                newline.append(self.matrix[line][item] + other.matrix[line][item])
            result_matrix.append(newline)
        return result_matrix



example1 = Matrix([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
    ])
example2 = Matrix([
    [4, 4, 4],
    [5, 5, 5],
    [6, 6, 6]
    ])

example_diff_size = Matrix([
    [1, 4, 2, 7],
    [5, 5, 5, 5],
    [6, 6, 6, 4]
])

print(example1)
print(example2)
example12 = Matrix(example1 + example2)
print(example12)

print(example1 + example_diff_size)