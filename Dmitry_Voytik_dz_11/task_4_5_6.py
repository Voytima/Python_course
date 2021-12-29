# 4.Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
class Store:
    def __init__(self, title):
        self.title = title
        self.list = {}
        self.to_go_list = []

# Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
    def tech_income(self, org_type):
        self.list.setdefault(org_type.group_name(), []).append(org_type)

    def tech_ordering(self, org_type):
        if self.list[org_type]:
            self.list.setdefault(org_type).pop(0)

    def tech_list(self, where):
        print(f"From {self.title} we allocated: {self.to_go_list} to {where}")


# Создать класс «Оргтехника», который будет базовым для классов-наследников.
# В базовом классе определить параметры, общие для приведённых типов.
class OfficeTech:
    def __init__(self, title, model):
        self.title = title
        self.model = model
        self.group = self.__class__.__name__

    def group_name(self):
        return f"{self.group}"

    def __repr__(self):
        return f'{self.title} {self.model}'


# Классы-наследники — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Printer(OfficeTech):
    def __init__(self, title, model, p_type):
        super().__init__(title, model)
        self.p_type = p_type

    def __repr__(self):
        return f"Printer: {self.title} {self.model}; {self.p_type}"


class Scanner(OfficeTech):
    def __init__(self, title, model, transmitter):
        super().__init__(title, model)
        self.transmitter = transmitter

    def __repr__(self):
        return f"Scanner: {self.title} {self.model} with {self.transmitter}"


class Copier(OfficeTech):
    def __init__(self, title, model, speed):
        super().__init__(title, model)
        self.speed = speed

    def __repr__(self):
        return f"Copier: {self.title} {self.model}; Copier speed: {self.speed}"


store = Store('Central Stock')
office = Store('Samsung office')
p = Printer('HP', 'LaserJet Pro M28a', 'laser')
p_1 = Printer('HP', 'LaserJet Pro M28w', 'laser')
s = Scanner('Epson', 'Perfection V600', 'CCD transmitter')
c = Copier('Xerox', 'B205', 30)

print("*" * 50)
print(p)
print(p_1)
print(s)
print(c)
print("*" * 50)
store.tech_income(p)
store.tech_income(p_1)
store.tech_income(s)
store.tech_income(c)
print(store.list)
print("*" * 50)
store.tech_ordering('Scanner')
store.to_go_list.append('Scanner')
store.tech_list(Store(office))
print("*" * 50)
print(store.list)
print("*" * 50)
