# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Wear:
    name: str
    type: str
    size: int
    height: int

    def __init__(self, name: str, type: str, size: int = None, height: int = None):
        self.name = name
        self.type = type
        self.size = size
        self.height = height

    @property
    def fabric_consumption(self):
        if self.type == "пальто":
            if self.size != None and isinstance(self.size, int):
                return round(self.size / 6.5 + .5, 2)
            else:
                print(f"Для {self.name} размер не указан, либо имеет неверный формат, вычислить расход ткани невозможно")
                return None
        elif self.type == "костюм":
            if self.height != None and isinstance(self.height, int):
                return round(2 * self.height + .3, 2)
            else:
                print(f"Для {self.name} рост не указан, либо имеет неверный формат, вычислить расход ткани невозможно")
                return None

coat_one = Wear("Наполеон", "пальто", 38, None)
coat_two = Wear("Кутузов", "пальто", 54, None)
suit_one = Wear("Тройка", "костюм", None, 180)
suit_two = Wear("Фрак", "костюм", None, 165)

wears = ["coat_one", "coat_two", "suit_one", "suit_two"]

print(f"расход ткани на {coat_one.type} {coat_one.name} {coat_one.fabric_consumption}")
print(f"расход ткани на {coat_two.type} {coat_two.name} {coat_two.fabric_consumption}")
print(f"расход ткани на {suit_one.type} {suit_one.name} {suit_one.fabric_consumption}")
print(f"расход ткани на {suit_two.type} {suit_two.name} {suit_two.fabric_consumption}")

print(Wear)
