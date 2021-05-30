# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т

class Road():
    length: int
    width: int
    one_square_meter_weight: int
    thinkness: int

    def __init__(self, length, width, one_square_meter_weight=25, thinkness=1):
        self.length = length
        self.width = width
        self.one_square_meter_weight = one_square_meter_weight
        self.thinkness = thinkness

    def weight(self):
        print(f"Масса асфальта = {(self.width * self.length * self.one_square_meter_weight * self.thinkness) / 1000} т")

def_road = Road(100, 10)
another_road = Road(5000, 20, 25, 5)

def_road.weight()
another_road.weight()



