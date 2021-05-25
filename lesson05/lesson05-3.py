# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('lesson05-3-sample.txt') as my_file:
    salary = []
    print("фамилии сотрудников с окладом менее 20 тыс:")
    for line in my_file.readlines():
        formated_line = line.replace("\n", "")
        # print(formated_line)
        if float(formated_line.split()[1]) < 20000:
            print(f"{formated_line.split()[0]}  \t\t\tс результатом: {formated_line.split()[1]}")
        salary.append(float(formated_line.split()[1]))
    print(f"величина среднего дохода сотрудников: {round(sum(salary) / len(salary), 2)}")


