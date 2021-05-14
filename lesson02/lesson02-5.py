# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2]
answer = "y"
while answer == "y":
    new_rating_value = input("Введите новый элемент рейтинга, натуральное число >>>")
    if not new_rating_value.isdigit():
        print("Неверный формат")
        exit()
    new_rating_value = int(new_rating_value)
    rating.append(new_rating_value)
    rating.sort()
    rating.reverse()
    print(rating)
    answer = input("добавить новый элемент рейтинга? y/n >>")
