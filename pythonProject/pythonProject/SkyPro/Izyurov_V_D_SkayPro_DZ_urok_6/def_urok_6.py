import random

def writ_words(fileneme):
    '''Функция читает файл и выводит его в список

    Параметры:
    ---------
    Вход: Файл со словами для вопросов, .txt
    Выход:Список из слов файла, list
    '''
    lint_fileneme = []
    new_line = []

    with open(fileneme, 'r', encoding='utf8') as f:
        line_fileneme = f.readlines()
        for line in line_fileneme:
            new_line.append(line.strip('\n'))
    return new_line


def shuffle_words(words):
    '''Функция берет список слов и перемешивает буквы в словах и возвращает в список

    Параметры:
    ---------
    Вход: Список со словами для вопросов, list
    Выход:Список с перемешенными словами для вопросов, list
    '''
    new_word_list = []

    for word in words:
        word_list = list(word)
        random.shuffle(word_list)
        new_word_list.append(''.join(word_list))
    return new_word_list


def ask_questions(shuffle_list, list):
    '''Функция задает вопросы и формирует статистику по ответам

    Параметры:
    ---------
    Вход: Два списка со словами (Перевернутые слова и правильные слова, list
    Выход:Список количеством правильных ответов и баллов, list
    '''
    numbers = 0
    num_question = 0
    score = 0

    for question in shuffle_list:
        answer_question = input(f'''\nУгадайте слово: {question}
Ваш ответ: ''')
        if answer_question == list[numbers]:
            print('Ответ верный, + 10 баллов')
            numbers += 1
            num_question += 1
            score += 10
        else:
            print(f'Ответ не верный, правильный ответ {list[numbers]}')
    return f'{num_question}:{score}:'


def writ_file(list):
    '''Функция записывает статистику в файл

    Параметры:
     ---------
    Вход: Строка с данными, str
    Выход:-
    '''

    with open('history.txt', 'a', encoding='utf8') as f:
        f.write(f'{list} \n')


def statistics_output(fileneme):
    '''Функция читает файл, подсчитывает топ по балам и количеству вопросов и выводит результат

    Параметры:
    ---------
    Вход: файл со статистикой, .txt
    Выход: Строка с текстом, str
    '''
    max = 0
    count = 0

    with open('history.txt', 'r', encoding='utf8') as f:
        for line in f:
            line_list = line.strip().split(':')
            if int(line_list[1]) > int(max):
                max = int(line_list[1])
            if int(line_list[0]) > int(count):
                count = int(line_list[0])

        return f'''{line_list[2]},
Наилучший результат:
количество вопросов: {count} 
количество баллов: {max} '''

