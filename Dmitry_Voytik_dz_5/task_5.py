from collections import Counter

# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Var_1
result = []
result_p = [result.append(num) for num in src if src.count(num) == 1]
print(src)
print(result)

# Var_2
how_many = Counter(src)
result_opt = [i for i, j in how_many.items() if j == 1]
print(result_opt)