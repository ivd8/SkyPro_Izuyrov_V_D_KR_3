import random

user = {}
user_login = {}
user_login_dir = []
username = None
user_password = None
dictionary_questions = {}
count_response = {}
answers_to_question = {}

morse_code = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.",
    "(": "-.--.", ")": "-.--.-"
}

dictionary_for_questions = ['life', 'hour', 'code', 'bit', 'list', 'soul',
                            'next', 'week', 'day', 'night', 'month', 'year', 'time', 'world',
                            'sun', 'animal', 'tree', 'water', 'food', 'fire', 'country', 'city',
                            'street', 'work', 'school', 'shop', 'house', 'room', 'car', 'paper',
                            'pen', 'door', 'chair', 'table', 'money', 'way', 'end', 'price',
                            'question', 'answer', 'number', 'be', 'have', 'do', 'get', 'can',
                            'feel', 'live', 'love', 'want', 'say', 'tell', 'see', 'hear', 'listento',
                            'believe', 'take', 'give', 'go', 'run', 'walk', 'come', 'leave', 'sit',
                            'stand', 'make', 'know', 'understand', 'remember', 'think', 'bring',
                            'find', 'lose', 'use', 'work', 'study', 'learn', 'ask', 'answer',
                            'let', 'help', 'begin', 'play', 'write', 'read', 'turn', 'meet',
                            'change', 'stop', 'open', 'close', 'always', 'never', 'also', 'just',
                            'only', 'again', 'often', 'still', 'already', 'almost', 'enough',
                            'very', 'sometimes', 'now', 'then', 'usually', 'quickly', 'slowly',
                            'well', 'especially'
                            ]


# == ФУНКЦИИ ДЛЯ: [1] ВХОД ======================================================

# Функция проверки фхода
def login_account():
    """
    Функция проверяет, имеется ли созданный аккаунт с логином и паролем
    и если таковы совпадают, заходит в игру через активированный аккаунт.
    """

    user_login_dir = {}
    while True:
        user_login_local = str(input('\nВведите Имя пользователя: '))
        password_login = str(input('Введите Пароль пользователя: '))
        user_login_dir[user_login_local] = password_login

        for k, v in user.items():
            if {k: v} == user_login_dir:
                print(user_login_dir)
                return user_login_dir
                break
            else:
                print('\n\n| Такого пользователя не обнаружили. Неправильный логин или пароль. \n| ПОПРОБУЙТЕ ЕЩЕ РАЗ.')
                continue


# == ФУНКЦИИ ДЛЯ: [2] РЕГЕСТРАЦИЯ ===============================================

# Функция регистрации
def account_registration():
    """
    Функция регистрирует пользователя и проверяет не занято ли имя пользователя
    для регистрации.
    """

    while True:
        username = str(input('Введите имя пользователя: '))
        if username in user:
            print('Такой пользователь уже существует')
            continue
        elif username != user.keys:
            return username
            break


# Функция проверки пароля
def user_password_reliability():
    """
    Функция проверяет, надежность придуманного пароля.
    """

    while True:
        user_password = str(input('''Придумайте надежный пароль для аккаунта:
        Пароль должен содержать как минимум одну маленькую и одну большую букву.
        А также иметь хотя бы одну цифру и специальный символ. Пароль не должен 
        быть короче 8 символов
        НАПИШИТЕ ПАРОЛЬ: '''))

        password_security = {1: None, 2: None, 3: None, 4: None}
        password_security_check = {1: True, 2: True, 3: True, 4: True}
        if len(user_password) >= 8:
            for i in user_password:
                if i.islower() == True:
                    password_security[1] = True
                if i.isupper() == True:
                    password_security[2] = True
                if i.isnumeric() == True:
                    password_security[3] = True
                if i in ".,:;!_*-+()/#¤%&":
                    password_security[4] = True

            if password_security == password_security_check:
                print('Все ок')
                return user_password
                break
            else:
                print('Пароль не надежен')
        else:
            print('Пароль должен быть больше 8 символов')


# Функция сравнения паролей
def password_comparison():
    """
    Функция проверяет идентичность повторного пароля.
    """

    while True:
        password_comparison = str(input('ВВЕДИТЕ ПАРОЛЬ ПОВТОРНО: '))

        if user_password == password_comparison:
            print('Все ок')
            return password_comparison
            break

        else:
            print('Пароль не совподает, введите еще раз')
            continue


# == ФУНКЦИИ ДЛЯ ИГРЫ ===========================================================

# Функция для подтврждения Играть
def ready_to_play():
    """
    Функция спрашивает подтверждение для игры.
    """

    while True:
        variable_variable = int(input('''\nСегодня мы потренируемся расшифровывать азбуку Морзе. 
        Если ты готов начать введи соответствующую цифру из Меню.

[1] Да, я готов !!!
[2] Нет, это не для меня !!!

ВВЕДИТЕ ЧИСЛО: '''))
        if variable_variable == 1:
            print('\nИгра началась.')
            break
        elif variable_variable == 2:
            pass
        else:
            print('\nТакой цифры в меню НЕТ, попробуйте еще раз. ')
            continue


# Функция создания словаря с ключами Морзе
def dictionary_questions():
    """
    Функция создает словарь со значениемя из азбуки морзе. Словарь с вопросами
    можно добавлять сколько угодно.
    """

    dictionary_questions = {}

    for i in dictionary_for_questions:
        variable_dictionary = []
        dictionary_questions_key_val = []
        dictionary_questions_val = []

        for i_2 in i:
            i_2_replace = i_2.replace(i_2, morse_code[i_2])
            variable_dictionary.append(i_2_replace)
            dictionary_questions_val = ''.join(variable_dictionary)
            dictionary_questions[i] = dictionary_questions_val
    return dictionary_questions


# Функция рандомных 4 - х вопросов c вариантами ответов
def questions_1():
    """
    Функция создает рандомные 4 ключа со значениеми, 4 раза, для заданий с выбором
    ответов. Проводит задание с выбором ответов.
    """

    questions_1 = []
    count_response_1 = []

    for i in range(4):
        for i_1 in range(1):
            right_question_keys = random.choice(list(dictionary_questions.keys()))
            right_question_values = dictionary_questions[right_question_keys]
            questions_1.append(right_question_values)

            for i_2 in range(3):
                response_options_values = random.choice(list(dictionary_questions.values()))
                questions_1.append(response_options_values)

        random.shuffle(questions_1)

        while True:
            variable_response = int(input(f'''\nВопрос: Как, на языке Морзе, будет писаться слово: {right_question_keys}

Выберете правильный ответ и введите цифру

[1] {questions_1[0]}
[2] {questions_1[1]}
[3] {questions_1[2]}
[4] {questions_1[3]}
[5] Правильный ответ для отладки программы {right_question_values}

    ВВЕДИТЕ ОТВЕТ: '''))

            if variable_response == 1:
                if questions_1[0] == right_question_values:
                    count_response_1.append(True)
                    print('\nОтвет верный')
                    break
                else:
                    count_response_1.append(False)
                    print('\nОтвет неверный')
                    break

            elif variable_response == 2:
                if questions_1[1] == right_question_values:
                    count_response_1.append(True)
                    print('\nОтвет Верный')
                    break
                else:
                    count_response_1.append(False)
                    print('\nОтвет неверный')
                    break

            elif variable_response == 3:
                if questions_1[2] == right_question_values:
                    count_response_1.append(True)
                    print('\nОтвет Верный')
                    break
                else:
                    count_response_1.append(False)
                    print('\nОтвет неверный')
                    break

            elif variable_response == 4:
                if questions_1[3] == right_question_values:
                    count_response_1.append(True)
                    print('\nОтвет Верный')
                    break
                else:
                    count_response_1.append(False)
                    print('\nОтвет неверный')
                    break

            elif variable_response == 5:
                if right_question_values == right_question_values:
                    count_response_1.append(True)
                    print('\nОтвет Верный')
                    break

                else:
                    count_response_1.append(False)
                    print('\nОтвет неверный')
                    break
            else:
                print('\nТакой цифры НЕТ, введите еще раз')
                continue

    return count_response_1


# Функция рандомных 4 - х вопросов с одним ответом на вопрос
def questions_2():
    """
    Функция создает рандомные четыре ключа со значениями для заданий с написанием
    ответов. Проводит задание с написанием ответов.
    """

    count_response_2 = []

    for i in range(4):
        right_question_keys = random.choice(list(dictionary_questions.keys()))
        right_question_values = dictionary_questions[right_question_keys]

        while True:
            variable_response = input(f'''Как будет писатся слово {right_question_keys} 
(Правильный отввет для отладки: {right_question_values})

ВВЕДИТЕ ОТВЕТ: ''')

            if variable_response == right_question_values:
                count_response_2.append(True)
                print('\nОтвет Верный')
                break

            else:
                count_response_2.append(False)
                print('\nОтвет не верный')
                break

    return count_response_2


# == ФУНКЦИИ ПОДСЧЕТ СТАТИСТИКИ =================================================

# Функция для подсчета статистики
def print_statistics():
    """
    Функция подсчитывает статистику по ответам
    """

    right_answers_1 = answers_to_question[username][1].count(True)
    right_answers_2 = answers_to_question[username][2].count(True)
    fault_answers_1 = answers_to_question[username][1].count(False)
    fault_answers_2 = answers_to_question[username][2].count(False)
    print(f'''\n{username}, 
Вы решили {right_answers_1 + right_answers_2} вопросов из {fault_answers_1 + fault_answers_2 + right_answers_1 + right_answers_2}.
Вы решили {(right_answers_1 + right_answers_2) / (fault_answers_1 + fault_answers_2 + right_answers_1 + right_answers_2) * 100} процентов вопросов.
Вы набрали {right_answers_1 + (right_answers_2 * 2)} баллов из {fault_answers_1 + right_answers_1 + (fault_answers_2 + right_answers_2) * 2}''')


# == НАЧАЛО КОДА (МЕНЮ ВХОД-РЕГЕСТРАЦИЯ) ========================================

while True:
    entry_menu = int(input('''\n====== МЕНЮ ВХОДА ======
[1] Вход 
[2] Регистрация

ВВЕДИТЕ ЧИСЛО: '''))

    # [1] Вход
    if entry_menu == 1:
        user_login = login_account()
        break

    # [2] Регистрация
    elif entry_menu == 2:
        username = account_registration()
        user_password = user_password_reliability()
        password_comparison = password_comparison()
        user[username] = password_comparison
        print(user)
        continue

    elif entry_menu != 1 or entry_menu != 2:
        continue

# == (МЕНЮ ЮЗЕРА, ИГРА, СТАТИСТИКА) =============================================

while True:
    entry_menu = int(input(f'''\n====== МЕНЮ ЮЗЕРА ======
Привет, {username}, выбери необходимый пункт из Меню и введи число!

[1] Начать игру 
[2] Посмотреть статистику
[3] Выход из аккаунта

ВВЕДИТЕ ЧИСЛО: '''))

    # [1] Начать Игру
    if entry_menu == 1:
        ready_to_play()
        dictionary_questions = dictionary_questions()
        answers_to_question_1 = questions_1()
        answers_to_question_2 = questions_2()
        answers_to_question[username] = {1: answers_to_question_1, 2: answers_to_question_2}


    # [2] Посмотреть статистику
    elif entry_menu == 2:
        print_statistics()

# [3] Выход из аккаунта
