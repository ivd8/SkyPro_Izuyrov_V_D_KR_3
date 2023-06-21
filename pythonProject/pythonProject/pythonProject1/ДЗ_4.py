
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
word = {}
level = {}
answers = {}
message_level = ''

while message_level not in ["легкий", "средний", "сложный"]:
    #if message_level is not ["легкий", "средний", "сложный"]:
    print('Выберите уровень сложности. \nЛегкий, Средний, Сложный')
    message_level = input('Введите ответ: ').lower()

if message_level in ['легкий']:
    level = words_easy

elif message_level in 'средний':
    level = words_medium

elif message_level in 'сложный':
    level = words_hard



for k, v in level.items():
    k_1 = k.title()
    v_1 = (v[0] + '*' * (len(v) - 1)).title()
    print(f'''\n\n{k_1}, {len(v_1)} букв, начинается на {v_1}''')
    i = input('Введите ответ: ').lower()

    while i in[v]:
        if  i  not in [v]:
            print(f'Программа: Неверно. {k_1}  — это {v_1}.')
            answers[k] = v
            word[k] = False

        elif i in [v]:
            print(f'Программа: Верно, {k_1} — это {v_1}.')
            answers[k] = v
            word[k] = True

for i in answers:
    print answers.keys()

print(message_level)
print(word)
print(answers)