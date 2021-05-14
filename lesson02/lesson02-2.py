# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
# на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
import random

length = input("введите количество элементов >>>")

if not length.isdigit():
    print("Неверный формат числа")
    exit()

length = int(length)

new_list = []
i=0
while i < length:
    new_list.append(input("введите элемент списка >>>"))
    i += 1
print(new_list)

for i in range(0, length, 2):
    if i < length - 1:
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]

print(new_list)



