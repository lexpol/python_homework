# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker():
    name: str
    surname: str
    position: str
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, positon, _income):
        self.name = name
        self.surname = surname
        self._income = _income

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])

patrick = Worker("Patrick", "Brr", "logist", {"wage": 1000, "bonus": 200})
steve = Worker("Steve", "Fu", "founder", {"wage": 5000, "bonus": 700})

Position.get_full_name(patrick)
Position.get_total_income(patrick)
Position.get_full_name(steve)
Position.get_total_income(steve)