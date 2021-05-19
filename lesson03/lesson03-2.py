# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birth_year, city, email, phone):
    """функция для вывода данных о пользователе одной строкой"""
    print(f"имя: {name}, фамилия: {surname}, год рождения: {birth_year}, "
          f"город проживания: {city}, email: {email}, телефон: {phone}")

try:
    name_in = str(input("Введите Имя >>> "))
    surname_in = str(input("Введите Фамилию >>> "))
    year_in = int(input("Введите год рождения >>> "))
    city_in = str(input("Введите Город проживания >>> "))
    email_In = str(input("Введите email >>> "))
    phone_In = str(input("Введите телефон >>> "))
    user_info(name = name_in,
              surname = surname_in,
              birth_year = year_in,
              city = city_in,
              email = email_In,
              phone = phone_In)
except ValueError:
    print("Неверный ввод!")