class Stationery:
    def __init__(self, title='Канцелярщина'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'А не написать ли нам что-нибудь с помощью {self.title} ручки?!')


class Pencil(Stationery):
    def draw(self):
        print(f'А не нарисовать ли нам что-нибудь с помощью карандашика {self.title}?!')


class Handle(Stationery):
    def draw(self):
        print(f'А не напакостить ли нам что-нибудь на обоях в гостиной с помощью маркера {self.title}?!')


stationery = Stationery()
pen = Pen("крутой")
pencil = Pencil("HB pencil")
handle = Handle("edding 390")

all_together = [stationery, pen, pencil, handle]

for i in all_together:
    i.draw()
