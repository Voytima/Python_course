# 4.Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так
from functools import wraps


def val_checker(a_func):
    def val_checker_2(func):

        @wraps(func)
        def w_func(num):
            if a_func(num):
                print(func(num))
            else:
                raise ValueError(f'incorrect value {num}')
        return w_func
    return val_checker_2


@val_checker(lambda n: n > 0)
def calc_cube(n):
    return n ** 3


try:
    x = calc_cube(2)
except ValueError as e:
    print(e)

# сможете ли вы замаскировать работу декоратора?

print(help(calc_cube))