# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = ""
    def running(self):
        modes = {"red   ": 7, "yellow": 2, "green ": 5}
        # modes = {"yellow": 7, "red   ": 2, "green ": 5} #раскомментировать для проверки последовательности цветов
        check_mode = []
        for __color, time in modes.items():
            self.__color = __color
            check_mode.append(self.__color)
            print(f"\n{self.__color}  ", end="")
            for delay in range(time):
                print(".", end="")
                sleep(1)
        if check_mode == ['red   ', 'yellow', 'green ']:
            print(f"\n\nПоследовательность цветов верная")
        else:
            print(f"\n\nПоследовательность цветов нарушена")
            exit()

first_on_street = TrafficLight()

for iteration in range(5):
    print(f"\nИтерация {iteration}")
    first_on_street.running()




