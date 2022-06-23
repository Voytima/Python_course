# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
# Var_1
result = [int(num) for num in range(int(input("Enter any number: ")) + 1) if num % 2 != 0]
print(result)
# Var_2
result_2 = ([int(num) for num in range(int(input("Enter any number: ")) + 1) if num % 2 != 0])
print(*result_2, sep=', ')
