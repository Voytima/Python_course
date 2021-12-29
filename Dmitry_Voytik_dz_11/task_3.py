# 3.Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
class IntException(Exception):
    def __init__(self, info):
        self.info = info


num_list = []
while True:
    try:
        val = input("Enter any NUMBER ONLY: ")
        if val == 'quit':
            break
        if not val.isdigit():
            raise IntException("Only real numbers allowed")
        num_list.append(int(val))
    except IntException as err:
        print(err)
print()
print(f"\033[36m Final nums list:\n\033[0m{num_list}")
