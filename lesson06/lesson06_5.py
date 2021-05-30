# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Example:
    attr1: str
    attr2: int
    attr3: bool

    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def print_all_attr(self):
        print(
            f"атрибут1: {self.attr1}\n"
            f"атрибут2: {self.attr2}\n"
            f"атрибут3: {self.attr2}\n"
            )

value = Example("jgfd", 55, "yjtfjhg")

print(value.attr1)
print(value.attr2)
print(value.attr3)

value.print_all_attr()