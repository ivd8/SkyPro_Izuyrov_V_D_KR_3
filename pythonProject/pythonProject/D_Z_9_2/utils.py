import json
from question import Question


def reading_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        question_text = item["q"]
        complexity_issue = item["d"]
        correct_answer = item["a"]
        question = Question(question_text, complexity_issue, correct_answer)
        questions.append(question)
    return questions

def statistic(questions):
    score = 0
    count = 0
    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1
    return f'\nВот и всё!'\
           f'\nОтвечено {count} вопроса из 10'\
           f'\nНабрано баллов: {score}'