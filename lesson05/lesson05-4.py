# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('lesson05-4-sample.txt') as my_file:
    with open('lesson05-4-result.txt', 'w+') as result_file:
        for line in my_file.readlines():
            formatted_line = line.replace("\n", "").split()
            if formatted_line[0] in translate_dict:
                print(f"{translate_dict[formatted_line[0]]} {formatted_line[1]} {formatted_line[2]}", file=result_file)
        result_file.seek(0)
        print(result_file.read())