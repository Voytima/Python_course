# 2.Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class WrDivision(Exception):
    def __init__(self, info):
        self.info = info


try:
    dividend = int(input("Enter a dividend value: "))
    divisor = int(input("Enter a divisor value: "))
    if divisor == 0:
        raise WrDivision("Division by 0 forbidden!")
    quotient = dividend / divisor
except ValueError:
    print("That was not a number(s) (-_-)")
except WrDivision as wd:
    print(wd)
else:
    print(f"Division result: {quotient}")
