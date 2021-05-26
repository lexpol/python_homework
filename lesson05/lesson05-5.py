# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('lesson05-5-sample.txt', 'w+') as my_file:
    length = randint(10, 30)
    numbers = [randint(0, 100) for i in range(length)]
    print(' '.join([str(x) for x in numbers]), file=my_file)
    my_file.seek(0)
    print(f"Данные, прочитанные из файла:\n{my_file.read()}")
    my_file.seek(0)
    summ = 0
    for number in my_file.read().split():
        summ += int(number)
    print(f"Сумма чисел в файле: {summ}")