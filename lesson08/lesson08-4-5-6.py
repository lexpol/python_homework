# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class CompanyDivision:
    name: str
    items: list

    def __init__(self, name):
        self.name = name
        self.items = []

class CapacityExeption(Exception):
    def __init__(self, current, needed):
        self.current = current
        self.needed = needed

    def __str__(self):
        return f"Not enough space, current = {self.current}, need = {self.needed}"

class ValueExeption(Exception):
    pass

class Warehouse:
    max_items: int
    items: list

    def __init__(self, count = 0):
        self.max_count = count
        self.items = []

    def store(self, items: dict):
        if len(self.items) >= self.max_count:
            raise CapacityExeption(len(self.items), len(self.items) + len(items))
        elif len(items) > (self.max_count - len(self.items)):
            raise CapacityExeption(self.max_count, len(self.items) + len(items))
        self.items.extend(items)

    def move(self, item_pos, division):
        division.items.append(self.items[item_pos])
        self.items.pop(item_pos)

class OfficeEquipment:
    item_name: str
    color: str
    price: int
    max_paper_size: str

    def check_input(self):
        if str(self.price).isdigit():
            return "check passed"
        else:
            raise ValueExeption

class Printer(OfficeEquipment):
    paper_capacity: int

    def __init__(self, item_name, color, price, max_paper_size, paper_capacity = 100):
        self.item_name = item_name
        self.color = color
        self.price = price
        self.max_paper_size = max_paper_size
        self.paper_capacity = paper_capacity

class Scaner(OfficeEquipment):

    def __init__(self, item_name, color, price, max_paper_size):
        self.item_name = item_name
        self.color = color
        self.price = price
        self.max_paper_size = max_paper_size

class Copier(OfficeEquipment):
    paper_capacity: int

    def __init__(self, item_name, color, price, max_paper_size, paper_capacity = 100):
        self.item_name = item_name
        self.color = color
        self.price = price
        self.max_paper_size = max_paper_size
        self.paper_capacity = paper_capacity



stock = Warehouse(5)
bookkeeping = CompanyDivision("bookkeeping")
hp = Printer("HP", "Black", 200, "A4", 200)
mustek = Scaner("Mustek", "White", 150, "A3")
xerox = Copier("Xerox", "Gray", 500, "A4", 500)
item_list = [hp.__dict__, mustek.__dict__, xerox.__dict__]

try:
    stock.store(item_list)
except CapacityExeption as exception:
    print(f"Not enough space, need: {exception.needed - exception.current} more")

print(f"состояние склада до перемещения техники: \n{stock.items}")
stock.move(0, bookkeeping)
print(f"Позиция: \n{bookkeeping.items}\nперемещена в отдел бухгалтерии")
print(f"состояние склада после перемещения техники: \n{stock.items}")

epson = Printer("Epson", "Blue", "one hundred", "A4", "fifth")

try:
    print(epson.check_input())
except ValueExeption:
    print(f"проверка не пройдена, для {epson.item_name} параметр price должен быть числовым")

