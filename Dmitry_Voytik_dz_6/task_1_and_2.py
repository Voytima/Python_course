# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# Получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
# 2.* Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из задания 1.
from collections import Counter

with open('parsed_nginx.txt', 'w', encoding='utf-8') as parsed_doc:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_doc:
        text = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in log_doc)
        for i in text:
            print(i, file=parsed_doc)

'''
Создадим словарь и в нем с помощью Counter найдем 
IP-адрес спаммера и посчитаем кол-во запросов от него
'''

with open('parsed_nginx.txt', 'r', encoding='utf-8') as parsed_doc:
    spam_dict = Counter()
    for _ in parsed_doc:
        spam_dict[_.split()[0]] += 1
    ip, cases = spam_dict.most_common(1)[0][0], spam_dict.most_common(1)[0][1]
    print(f"Spam IP: {ip}\nEntries number: {cases}")
