# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('lesson05-6-sample.txt') as my_file:
    dict = {}
    for line in my_file.readlines():
        hours = []
        for item in line.split():
            time = ""
            for symbol in item:
                if symbol.isdigit():
                    time += symbol
                elif time != "":
                    hours.append(int(time))
                    time = ""
        key = line.replace("\n", "").split()[0].replace(":", "")
        value = sum(hours)
        dict.update({key: value})
    print(dict)