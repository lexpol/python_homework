# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
import json

with open('lesson05-7-sample.txt') as my_file:
    profits = []
    profit = 0
    firm_dict = {}
    for line in my_file.readlines():
        profit = (float(line.split()[2]) - float(line.split()[3]))
        print(f"Выручка {line.split()[0]} {profit}")
        firm_dict.update({line.split()[0]: profit})
        if profit > 0:
            profits.append(profit)
    average_profit = round(sum(profits) / len(profits), 2)
    print(f"\nСредняя прибыль: {average_profit}")
result_list = [firm_dict, {'average_profit': average_profit}]
with open('lesson05-7-result.json', 'w') as file_stream:
    json.dump(result_list, file_stream)
