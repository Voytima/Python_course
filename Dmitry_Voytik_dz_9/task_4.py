from random import choice


class Car:
    directions = ['на Север', 'на Юг', 'на Запад', 'на Восток', 'в Нарнию']

    def __init__(self, s, c, n, i_p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} повернула {choice(self.directions)}")

    def show_speed(self):
        return f"Машина {self.name} двигается со скоростью {self.speed} без нарушений"


class TownCar(Car):

    def show_speed(self):
        return f"{self.name} двигается со скоростью {self.speed} и получит штрафака!" if self.speed > 60 \
            else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f"{self.name} двигается со скоростью {self.speed} и получит штрафака!" if self.speed > 40 \
            else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

    def __init__(self, s, c, n):
        super().__init__(s, c, n, i_p=True)


town_car = TownCar(65, "белый", "FW Juke")
work_car = WorkCar(20, "желтый", "Aсфальтоукладчик")
sport_car = SportCar(140, "красный", "BMW X7")
police_car = PoliceCar(80, "сине-белый", "Бобик")

all_cars = [town_car, work_car, sport_car, police_car]

for i in all_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.turn()
    i.turn()
    i.stop()
    print()
