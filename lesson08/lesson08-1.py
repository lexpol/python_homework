# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    date: str
    day: int
    month: int
    year: int

    def __init__(self, date):
        self.date = date

    @staticmethod
    def check_date_format(date):
        if date[0] not in range(1, 31) and date[1] not in range(1, 12):
            print("wrong date format")
            exit()
        else:
            return date

    @classmethod
    def to_num(cls, date):
        return cls.check_date_format(list(map(int, date.replace('-', ' ').split())))

date_example = "22-01-1980"
date_wrong = "44-55-66"

print(Date.to_num(date_example))
print(Date.to_num(date_wrong))
