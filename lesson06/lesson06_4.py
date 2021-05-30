# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена!!!   ", end = "")
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена!!!  ", end = "")
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

toyota = TownCar(80, "red", "Toyota")
toyota.show_speed()
toyota.go()
toyota.turn("налево")
toyota.stop()

nissan = TownCar(50, "green", "Nissan")
nissan.show_speed()

ford = PoliceCar(120, "white", "Ford")
ford.show_speed()

ferrari = SportCar(180, "red", "Ferrari")
ferrari.show_speed()

kamaz = WorkCar(35, "dirty", "Kamaz")
kamaz.show_speed()

priora = WorkCar(160, "black", "Priora")
priora.show_speed()