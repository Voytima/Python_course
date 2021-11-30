#(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
dictionary = {
    'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
    'ten': 'десять'
    }


def num_translate_adv(num):
    """
    Та же функция, но с доп.действием и со словарем снаружи

    :func .istitle: проверит если параметр(ввод) будет начинаться с заглавной буквы

    """

    if num.istitle():
        return str(dictionary.get(num.lower())).title()
    return dictionary.get(num)


print(num_translate_adv(input('Enter any number with letters from zero to ten: ')))