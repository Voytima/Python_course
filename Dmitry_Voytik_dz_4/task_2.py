from requests import get, utils
from decimal import *

response = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val_code):
    content = response.split('<Valute ID=')
    for n in content:
        if val_code.upper() in n:
            print(val_code.upper(), end=' --> ')
            result = Decimal(n.replace('/', '').split('<Value>')[1].replace(',', '.')).quantize(Decimal('1.00'))
            return result


print(currency_rates('usd'))
print(currency_rates('EuR'))
