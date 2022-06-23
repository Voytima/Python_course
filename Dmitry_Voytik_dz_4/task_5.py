from requests import get, utils
from decimal import *
from datetime import datetime
from sys import argv

response = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val_code):
    content = response.split('<Valute ID=')
    for n in content:
        if val_code.upper() in n:
            print(datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date(), end=' ')
            print(val_code.upper(), end=' --> ')
            result = Decimal(n.replace('/', '').split('<Value>')[1].replace(',', '.')).quantize(Decimal('1.00'))
            return result

# Импортируем task_5 в Terminal


if __name__ == "__main__":
    cmd_input = argv[1]
    print(currency_rates(cmd_input))
