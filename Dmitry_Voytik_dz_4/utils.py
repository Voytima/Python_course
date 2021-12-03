from requests import get, utils
from decimal import *
from datetime import datetime

response = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val_code):
    content = response.split('<Valute ID=')
    for n in content:
        if val_code.upper() in n:
            print(datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date(), end=' ')
            print(val_code.upper(), end=' --> ')
            result = Decimal(n.replace('/', '').split('<Value>')[1].replace(',', '.')).quantize(Decimal('1.00'))
            return result


if __name__ == "__main__":
    print(currency_rates('usd'))
    print(currency_rates('EuR'))
else:
    print('*' * 28)
    print("I'm a currency_rates module!")
    print('*' * 28)
