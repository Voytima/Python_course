# 3.Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as u:
    with open('hobby.csv', 'r', encoding='utf-8') as h:
        if len(u.readlines()) >= len(h.readlines()):
            u.seek(0)
            h.seek(0)
            with open('user_hobby_task_3.txt', 'w', encoding='utf-8') as u_h:
                compare_list = zip_longest((" ".join(user.split(',')) for user in u), h, fillvalue=None)
                user_hobby = {str(i[0]).strip(): str(i[1]).strip() for i in compare_list}
                dump(user_hobby, u_h, ensure_ascii=False, indent=1)
                print(user_hobby)
        else:
            exit(1)
# 4.* Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО

with open('users.csv', 'r', encoding='utf-8') as u:
    with open('hobby.csv', 'r', encoding='utf-8') as h:
        compare_list = zip_longest((" ".join(user.split(',')) for user in u), h, fillvalue=None)
        with open('user_hobby_task_4.txt', 'w', encoding='utf-8') as u_h_4:
            for _ in compare_list:
                print({str(_[0]).strip(): str(_[1]).strip()}, file=u_h_4)