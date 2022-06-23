#Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
from random import randrange, choice


def get_jokes(n, repeat=False):
    """Функция генератора шуток, собирающая их из слов в трех списках

    :param n: количество шуток для генерации
    :param repeat: включать или исключать НЕ уникальные шутки
    :return: список уникальных (в данном случае) шуток, количество которых не превысит n

    """
    jokes = []
    noun = nouns.copy()
    adverb = adverbs.copy()
    adjective = adjectives.copy()
    melting_list = min(noun, adverb, adjective)

    while n and len(melting_list):
        point = randrange(len(melting_list))
        if repeat:
            jokes.append(f"{noun.pop(point)} {adverb.pop(point)} {adjective.pop(point)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n = (n - 1)
    return jokes


print(get_jokes(6, True))
#Документировать код функции.
#Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
