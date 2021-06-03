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
    _counter = 0
    _instances = []

    def __init__(self, name: str, type: str, size: int = None, height: int = None):
        self.name = name
        self.type = type
        self.size = size
        self.height = height
        self._instances.append(self)
        self._id = Wear._counter + 1
        Wear._counter += 1

    def __repr__(self):
        return f"расход ткани на {self.type} {self.name} {self.fabric_consumption}"

    def __iter__(self):
        return self

    def __next__(self):
        pass

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

total = 0
for item in Wear._instances:
    item_str = str(item)
    print(item_str)
    total += float(item_str.split()[5])
print(f"Общий расход ткани: {total}")
