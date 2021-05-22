# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
try:
    file, work_hours, hour_rate, bonus = sys.argv
except ValueError:
    print("invalid args")
    exit()

salary = (float(work_hours) * float(hour_rate)) + float(bonus)
print(f"salary = {salary}")