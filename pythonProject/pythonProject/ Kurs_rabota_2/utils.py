import random

import requests

from Basic_Word import BasicWord


def load_random_word(path=""):
    """ Функция получает список слов с внешнего
    ресурса, выберет случайное слово,
    создаст экземпляр класса `BasicWord`,
    возвращает этот экземпляр.
    Вход: json
    Выход: str, list
    """
    response = requests.get(path)
    response_json = response.json()

    response_json_random = random.choice(response_json)

    original_word = (response_json_random['word'])
    set_subwords = (response_json_random['subwords'])

    word = BasicWord(original_word, set_subwords)
    return word