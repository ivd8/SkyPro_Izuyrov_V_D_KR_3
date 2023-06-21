import json

def load_students(json):
    ''' Загружает список студентов из файла

    Параметры:
    ---------
    Вход: .json
    Выход: dict
    '''

    with open('students.json') as f:
        load_students_json = json.load(f)
    return load_students_json


def load_professions(json):
    ''' Загружает список профессий из файла

    Параметры:
    ---------
    Вход: .json
    Выход: dict
    '''

    with open('professions.json') as f:
        load_professions_json = json.load(f)
    return load_professions_json


def get_student_by_pk(pk):
    ''' Получает словарь с данными студента по его pk

    Параметры:
    ---------
    Вход: int
    Выход: dict
    '''

    students_by_pk = load_students(json)
    for student in students_by_pk:
        if student['pk'] != pk:
            continue
        elif student['pk'] == pk:
            return student


def get_profession_by_title(title):
    ''' Получает словарь с инфо о профе по названию

    Параметры:
    ---------
    Вход: int
    Выход: dict
    '''

    profession_by_title = load_professions(json)
    for profession in profession_by_title:
        if profession['title'] not in title:
            continue
        elif profession['title'] in title:
            return profession


def check_fitness(student, profession):
    ''' Высчитывает разницу имеющих и не хватающих навыков + в процентном соотношении

    Параметры:
    ---------
    Вход: dict, dict
    Выход: dict
    '''

    intersection_skills = {
        "has": [],
        "lacks": [],
        "fit_percent": []
    }
    student_set = set(student["skills"])
    profession_set = set(profession["skills"])
    intersection_skills["has"] = student_set.intersection(profession_set)
    intersection_skills["lacks"] = profession_set.difference(student_set)
    intersection_skills["fit_percent"] = int(len(intersection_skills["has"]) / len(profession_set) * 100)
    return intersection_skills
