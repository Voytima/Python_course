from abc import ABC, abstractmethod


class Cloth(ABC):
    result = 0

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def cost(self):
        pass

    def __add__(self, other):
        Cloth.result += self.cost + other.cost
        return Costume(0)

    def __str__(self):
        res = Cloth.result
        return f"{res}"


class Costume(Cloth):
    @property
    def cost(self):
        return round(2 * self.par + 0.3) / 100


class Coat(Cloth):
    @property
    def cost(self):
        return round(self.par / 6.5) + 0.5


coat = Coat(44)
costume = Costume(182)
print(coat + costume + coat)
