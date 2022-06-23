# 1.Написать скрипт, создающий стартер (заготовку) для проекта
import os

# создаем каркас для проекта
pj_starter = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}
# key - основная папка в проекте - my_project
for key, val in pj_starter.items():
    if not os.path.exists(key):     # Проверка на наличие уже созданных папок
        for v in val:               # Надо вытащить название подпапок для создания в проекте
            for sub_f in v.keys():  # Они являются ключами в подсловаре. Достаем ключи
                os.makedirs(os.path.join(key, sub_f))   # Создаем директории (основная и подпапки)
