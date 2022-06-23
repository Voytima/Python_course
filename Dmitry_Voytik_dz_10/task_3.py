class Cell:
    def __init__(self, c_number):
        self.c_number = c_number

    def make_order(self, rows):
        for i in range(self.c_number):
            while self.c_number:
                return "\n".join(['❀' * rows for _ in range(self.c_number // rows)]) + \
                       "\n" + '❀' * (self.c_number % rows)

    def __str__(self):
        return f"{self.c_number}"

    def __add__(self, other):
        print("\033[32mTotal cell count after summing:\033[39m")
        return Cell(self.c_number + other.c_number)

    def __sub__(self, other):
        print("\033[31mTotal cell count after subtraction:\033[39m")
        return Cell(self.c_number - other.c_number) if self.c_number - other.c_number > 0 \
            else "Cannot do subtraction this way"

    def __mul__(self, other):
        print("\033[34mTotal cell count after multiplication:\033[39m")
        return Cell(self.c_number * other.c_number)

    def __floordiv__(self, other):
        print("\033[35mTotal cell count after division:\033[39m")
        return Cell(self.c_number // other.c_number) if other.c_number > 0 else "Zero division forbidden!"


cell_1 = Cell(16)
cell_2 = Cell(14)
print("\033[33m*\033[39m" * 40)
print(cell_1.make_order(5))
print("\033[33m*\033[39m" * 40)
print(cell_1 + cell_2)
print("\033[33m*\033[39m" * 40)
print(cell_1 - cell_2)
# print(cell_2 - cell_1) Проверка ошибки вычитания
print("\033[33m*\033[39m" * 40)
print(cell_1 * cell_2)
print("\033[33m*\033[39m" * 40)
print(cell_1 // cell_2)
# cell_2 = Cell(0)      Проверка деления на 0
# print(cell_1 // cell_2)
print("\033[33m*\033[39m" * 40)
