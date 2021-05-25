# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.
with open('lesson05-2-sample.txt') as my_file:
    print(f"\nСодержимое Файла: \n\n{my_file.read()}\n")

with open('lesson05-2-sample.txt') as my_file:
    lines = 0
    for line in my_file.readlines():
        formated_line = line.replace("\n", "")
        lines += 1
        words = 0
        for word in formated_line.split():
            words += 1
        print(f"В строке {formated_line} количество слов: {words}")
    print(f"всего строк: {lines}")


