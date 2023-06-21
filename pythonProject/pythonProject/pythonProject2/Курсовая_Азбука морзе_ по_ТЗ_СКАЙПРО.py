import random

answers = [] # Список куда записывается результаты правильности ответов

morse_code = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
              "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
              "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
              "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
              "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
              "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
              "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
              "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.",
              "(": "-.--.", ")": "-.--.-"}


words = ['life', 'hour', 'code', 'bit', 'list', 'soul',
        'next', 'week', 'day', 'night', 'month', 'year', 'time', 'world',
        'sun', 'animal', 'tree', 'water', 'food', 'fire', 'country', 'city',
        'street', 'work', 'school', 'shop', 'house', 'room', 'car', 'paper',
        'pen', 'door', 'chair', 'table', 'money', 'way', 'end', 'price',
        'question', 'answer', 'number', 'be', 'have', 'do', 'get', 'can',
        'feel', 'live', 'love', 'want', 'say', 'tell', 'see', 'hear', 'listento',
        'stand', 'make', 'know', 'understand', 'remember', 'think', 'bring',
        'find', 'lose', 'use', 'work', 'study', 'learn', 'ask', 'answer',
        'let', 'help', 'begin', 'play', 'write', 'read', 'turn', 'meet',
        'change', 'stop', 'open', 'close', 'always', 'never', 'also', 'just',
        'only', 'again', 'often', 'still', 'already', 'almost', 'enough',
        'very', 'sometimes', 'now', 'then', 'usually', 'quickly', 'slowly',
        'well', 'especially']


def get_word(words):
    '''
    Функция получает случайное слово из списка
    '''
    random_word = random.choice(words)
    return random_word


def translates_word(word):
    '''
    Функция переводит слово в Морзе
    '''
    translates_letter_list = []
    for letter in word:
        translates_letter_list.append(morse_code[letter])
    return ''.join(translates_letter_list)

def print_statistics(answers):
  '''
  Функция посчитает количество
  правильных и неправильных ответов
  и выведет статистику
  '''
  right_answers = answers.count(True)
  fault_answers = answers.count(False)

  print(f'\nВсего задачек: {len(answers)}')
  print(f'Правильных ответов: {right_answers}')
  print(f'Неправильных ответов: {fault_answers}')


input('''Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем''')

for number in range(5):
    word = get_word(words)
    translates_morze = translates_word(word)
    answer_question = input(f'''\nСлово {number + 1} - {translates_morze}
Ведите отвтет: ''')

    if answer_question == word:
        print(f'Верно, {word}')
        answers.append(True)
    elif answer_question != word:
        print(f'Ответ неверный. Правильный ответ {word}')
        answers.append(False)

print_statistics(answers)