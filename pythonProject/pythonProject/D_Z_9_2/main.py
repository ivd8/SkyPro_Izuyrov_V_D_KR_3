import random

from utils import reading_file, statistic

if __name__ == '__main__':
    filename = 'questions.json'
    questions = reading_file(filename)

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Ваш ответ: ')
        question.user_answer = user_answer
        print(question.build_feedback())
    print(statistic(questions))

