#Var_1 (в строку)
numbers = (15 * 3, 15 / 3, 15 // 2, 15 ** 2)
for i in numbers:
    print(type(i))
print('*' * 70)
#Var_2 (в строку)
numbers = (15 * 3, 15 / 3, 15 // 2, 15 ** 2)
print(list(map(type, numbers)))