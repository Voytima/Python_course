# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
def odd_to():
    """

    Функция будет принимать пользовательский ввод и выводить только
    нечетные числа во введенном диапазоне значений.

    """
    num = int(input('Enter any value: '))
    for i in range(1, num + 1, 2):
        yield i


for n in odd_to():
    print(n)
