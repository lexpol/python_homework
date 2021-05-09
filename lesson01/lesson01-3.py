# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = input("Введите число от 0 до 9   >>>")
double = digit + digit
triple = digit + digit + digit
sum = int(digit) + int(double) + int(triple)
print("Сумма n + nn + nnn будет равна, ",sum)