# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

new_file = open(r"lesson05-1-sample.txt", "w+")
while True:
    user_input = str(input("Введите строку, пустая строка - выход >>>\n"))
    if user_input == str(""):
        break
    else:
        if new_file.writable():
            new_file.writelines(user_input + "\n")
        else:
            "Файл недоступен для записи"
new_file.close()

new_file = open(r"lesson05-1-sample.txt", "r")
print(f"Записано в файл {new_file.name} следующее содержимое:")
print(new_file.read())
new_file.close()
