import random

def get_is_file():
    """
    Функция читает словарь, составляет список и выводит 1-ое слово.

    Параметры
    ---------
    Вход: Текстовой файл c словами для вопросов, words.txt, file
    Выход: Первое слово после перемешивания, str
    """
    with open("words.txt", 'r') as file:
        contents = [word_list.rstrip() for word_list in file]
        random.shuffle(contents)
        return contents[0]


def questions_displays_statistics(word):
    '''
    Функция перемешивает буквы в слове, задает вопросы и подсчитыват очки.

    Параметры
    ---------
    Вход: Случайное слово из тектового файла, word, str
    Выход: Очки за ответ на вопрос, count_local, int
    '''
    count_local = 0
    word_list = list(word)
    random.shuffle(word_list)
    shuffles_letters = ''.join(word_list)
    print(word)
    answer_user = input(f'''Угадайте какое тут написанно слово: {shuffles_letters}
Напишите отвте: ''')

    if answer_user == word:
        count_local += 10
        print('Верно! Вы получаете 10 очков')
    elif answer_user != word:
        print(f'Ответ не верный, правильный ответ {word}')
    return count_local



def score_check(result):
#def score_check(result):
    #result_list = result.split(:)
    #print(f'result_list {result_list}')
    #result_file = []
    #with open('history.txt', 'r') as file:
        #for data_words in file:
            #data_word = data_words.split(:)
            #if data_word[0] == result_list[0] and int(result_list[1]) > data_word[1]:

                #result_file.append()
        #return result_file


def updating_result_file():
    with open('history.txt', 'w') as file:
        file.write()




#def score_check(result):
    #with open('history.txt', 'r') as file:
        #result_list = list(result)
        #for data in file:
            #result_file = []
            #result_file.append(data) list(data)
            #if int(result_file[1]) > int(result_list[1]):


def result_record(result):
    '''
        Функция записывает параметры в техтовый файл history.txt.

        Параметры
        ---------
        Вход: Имя и количество баллов полученые за вопросы, result, str
        Выход: -
        '''
    with open('history.txt', 'a') as file:
        file.write(f'{result}\n')



#def