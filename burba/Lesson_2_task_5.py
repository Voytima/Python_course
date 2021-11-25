#Создать список, содержащий цены на товары (10–20 товаров), например:
prices = [57.8, 46.51, 97, 22.01, 24.06, 11.21, 79, 54.7, 66, 15.01, 40.0, 19, 45.4, 61, 46.6]
# A)
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
print('*' * 100)
rub_kop_prices = []
for i in prices:
    r, kk = f'{i:.2f}'.split('.')
    rub_kop_prices.append(f'{r} руб {kk} коп,')
print(' '.join(rub_kop_prices))
print('*' * 100)
# B) Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
print('*' * 100)
# C) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
new_prices = sorted(prices, reverse=True)
print(new_prices)
print('*' * 100)
# D)Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(new_prices[:5])
print(new_prices[:5][::-1])
print('*' * 100)