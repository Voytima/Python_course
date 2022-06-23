# Урок_1_задание_2
#часть_1
list_1 = []
sum_list_1 = 0
sum_list_2 = 0
list_2 = []


for a in range(1, 1000, 2):
    list_1.append(a ** 3)
# print(list_1)
for idx, num in enumerate(list_1):
    numsum = 0
    while num > 0:
        numsum += num % 10
        num //= 10
    if numsum % 7 == 0:
        sum_list_1 += list_1[idx]

print('Ответ на 1 условие задачи: ', sum_list_1)
print('*' * 39)
# часть_2

for b in list_1:
    list_2.append(b + 17)
# print(list_2)
for idx, num in enumerate(list_2):
    numsum = 0
    while num > 0:
        numsum += num % 10
        num //= 10
    if numsum % 7 == 0:
        sum_list_2 += list_2[idx]

print('Ответ на 2 условие задачи: ', sum_list_2)