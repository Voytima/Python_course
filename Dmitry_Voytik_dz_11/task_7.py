# 7.Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.
class ComplexNumber(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return "%s, %sj" % (self.real, self.imag)

    def __add__(self, rhs):
        return ComplexNumber(self.real + rhs.real, self.imag + rhs.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                             self.imag*other.real + self.real*other.imag)


i = ComplexNumber(3, -4)
i_1 = ComplexNumber(5, 6)
summary = i + i_1
multiply = i * i_1
print('-' * 45)
print(f"Sum of two complex numbers is: ({i + i_1})")
print('-' * 45)
print(f"Multiply of two complex numbers is: ({i * i_1})")
print('-' * 45)
