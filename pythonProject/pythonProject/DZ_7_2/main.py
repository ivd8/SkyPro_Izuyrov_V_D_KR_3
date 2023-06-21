from utils import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    ''' Проверяет профпригодность студента к профессии

    Параметры:
    ---------
    Вход:  -
    Выход: -
    '''

    # Получаем входные данные о студенте
    pk = int(input('Введите номер студента: '))
    student = get_student_by_pk(pk)
    if student is None:
        print('У нас нет такого студента')
        quit()
    print(f'''\nСтудент {student['full_name']}
Знает {', '.join(student['skills'])}''')

    #Получаем входные данные о профессии
    title = input(f'\nВыберите специальность для оценки студента: ')
    profession = get_profession_by_title(title)
    if title is None:
        print('У нас нет такой специальности')
        quit()

    # Проверяем профпригодность студента к данной профессии
    intersection_skills = check_fitness(student, profession)
    if intersection_skills['fit_percent'] < 1:
        print(f'''\nПригодность 0%, нехватает необходимых навыков.
{student['full_name']} не знает {', '.join(profession['skills'])}''')
    else:
        print(f'''\nПригодность {intersection_skills['fit_percent']}%
{student['full_name']} знает {', '.join(intersection_skills['has'])}
{student['full_name']} не знает {', '.join(intersection_skills['lacks'])}''')

        print(intersection_skills)

main()
