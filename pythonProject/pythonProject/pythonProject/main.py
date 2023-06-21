i = "textascsdasdasdasd"
a = 1
counter = 0
score_counter = 0
interest_counter = int(counter / 3 * 100)   ### Не срабатывает коректно

name_user = input("Привет!" "\nПредлагаю проверить свои знания английского!" "\n\nНапиши, как тебя зовут. ")
print("\nПривет,", name_user, ", начинаем тренировку!", end="\n\n")


# Вопрос_№_1
for i in i:
    print("*******************************")
    print("* Вопрос 1: My name ___ Vova. *")
    print("*******************************")
    question_1 = str(input("\nВаш ответ: "))


    if question_1 == (""):
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")

    elif question_1.find(" ") == 1:
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")



    elif question_1 == "is":
        print("Ответ верный!", "\nВы получаете 10 баллов!", end="\n\n")
        counter += 1
        score_counter += 10
        break

    elif question_1.find(" ") == -1:
        print("Неправильно.", "\nПравильный ответ: is", end="\n\n")
        break


# Вопрос_№_2
for i in i:
    print("*******************************")
    print("*  Вопрос 2: I ___ a coder.   *")
    print("*******************************")
    question_2 = str(input("\nВаш ответ: "))

    if question_2 == (""):
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")
    elif question_2.find(" ") == 1:
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")


    elif question_2 == "am":
        print("Ответ верный!", "\nВы получаете 10 баллов!", end="\n\n")
        counter += 1
        score_counter += 10
        break
    elif question_2.find(" ") == -1:
        print("Неправильно.", "\nПравильный ответ: am", end="\n\n")
        break


# Вопрос_№_3
i = "Вопрос_№_3"

for i in i:
    print("*******************************")
    print("*Вопрос 3: I live ___ Moscow. *")
    print("*******************************")
    question_3 = str(input("\nВаш ответ: "))


    if question_3 == (""):
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")
    elif question_3.find(" ") == 1:
        print("ВВЕДИТЕ ОТВЕТ", end="\n\n")


    elif question_3 == "in":
        print("Ответ верный!", "\nВы получаете 10 баллов!", end="\n\n")
        counter += 1
        score_counter += 10
        break

    elif question_3.find(" ") == -1:
        print("Неправильно.", "\nПравильный ответ: in", end="\n\n")
        break

print(f'''Вот и всё, {name_user}! 
Вы ответили на {counter} вопросов из 3 верно.
Вы заработали {score_counter} баллов.
Это {int(counter / 3 * 100)} процентов.''')