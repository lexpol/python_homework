# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input("Введите строку из нескольких слов, разделённых пробелами >>>")
list = string.split()

for i in range(len(list)):
    if len(list[i]) > 10:
        long_word = list[i]
        list[i] = long_word[:10]

for i in enumerate(list):
    print(i)