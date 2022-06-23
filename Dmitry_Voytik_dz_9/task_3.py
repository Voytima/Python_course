class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return f'{sum(self._income.values())} $'


candidate = Position('Vasya', 'Pupkin', 'Cleaner', 200, 50)

print(candidate.position)
print(candidate.get_full_name())
print(candidate.get_total_income())
