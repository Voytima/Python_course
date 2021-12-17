# 3.Написать декоратор для логирования типов позиционных аргументов функции
from functools import wraps


def type_logger(func):
    @wraps(func)
    def w_func(*args, **kwargs):
        nums = [n for n in (*args, *kwargs.values())]
        output = [f"{func.__name__}({n}: {type(n)})" for n in nums]
        print(*output, *func(*args, **kwargs), sep='\n')
    return w_func


@type_logger
def calc_cube(*a, **b):
    nums = [n for n in (*a, *b.values()) if isinstance(n, int) or isinstance(n, float)]
    return [i ** 3 for i in nums]
# если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# для именованных аргументов?
# вывести имя функции?

cifer = calc_cube(5, 3.3, n=2)

# замаскировать работу декоратора?

print(help(calc_cube))
