# Урок_1_задание_3

for i in range(1, 101, 1):
    if i % 10 == 1 and i % 100 != 11:
        print(i, 'процент')
    elif 2 <= i % 10 <= 4 and not 11 < i % 100 < 15:
        print(i, 'процента')
    else:
        print(i, 'процентов')
