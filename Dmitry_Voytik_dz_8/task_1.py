# 1.Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
import re


def email_parse(email):
    RE_EMAIL = re.compile(r'(?P<username>([a-z]+))@(?P<domain>[^&]+\.[a-z]+)', re.IGNORECASE)
    if not RE_EMAIL.match(email):
        raise ValueError(f'incorrect email input: {email}')
    print(RE_EMAIL.match(email).groupdict())


emails = ['Картошка@мэйл.ру', 'someone@geekbrains.ru', 'someone@geekbrains,ru', 'someone@geekbrainsru']

for e in emails:
    try:
        email_parse(e)
    except ValueError as e:
        print(e)
